from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row
from ..core.models import CyclingFeature
from geojson_pydantic import Feature, FeatureCollection
from geoalchemy2 import functions
import json
from shapely import Polygon, unary_union, wkb
from ..core.cache import cache
from pydantic import BaseModel
from geopandas import GeoSeries

EARTH_RADIUS = 6378137


class GetFeaturesResponse(BaseModel):
    client_token: str
    collection: FeatureCollection


def parse_feat(f: Row):
    return Feature(**json.loads(f[0]))


def get_features(db: Session, requested_polygon: Polygon, client_id: int) -> FeatureCollection:
    cached = cache.get_item(client_id)

    if cached is None:
        query_polygon = requested_polygon
    elif cached.polygon.contains(requested_polygon):
        print('container', cached.polygon.boundary)
        return FeatureCollection(
            type="FeatureCollection",
            features=[]
        )
    else:
        query_polygon: Polygon = requested_polygon.difference(cached.polygon)
        print('difference', query_polygon.boundary)

    query = db.query(functions.ST_AsGeoJSON(CyclingFeature)).filter(
        functions.ST_Within(
            CyclingFeature.geometry,
            wkb.dumps(query_polygon, hex=True, srid=4326)
        )
    )

    if cached is None:
        cache.upsert_polygon_item(
            client_id, requested_polygon
        )
    else:
        cache.upsert_polygon_item(
            client_id,
            unary_union(
                [cached.polygon, requested_polygon]
            )
        )

    return FeatureCollection(
        type="FeatureCollection",
        features=list(
            map(parse_feat, query.all())
        )
    )
