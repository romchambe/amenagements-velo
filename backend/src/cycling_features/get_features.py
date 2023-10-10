from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row
from ..core.models import CyclingFeature
from ..core.request import WithToken
from geojson_pydantic import Feature, FeatureCollection
from geoalchemy2 import functions, Geography
import json
from shapely import Point, distance
from math import pi
from pydantic import BaseModel

EARTH_RADIUS = 6378137


class GetFeaturesResponse(BaseModel, WithToken):
    features: FeatureCollection


def parse_feat(f: Row):
    return Feature(**json.loads(f[0]))


def get_features(db: Session, bounds: list[float]) -> FeatureCollection:
    south_west = Point(bounds[0], bounds[1])
    north_east = Point(bounds[2], bounds[3])

    radius = distance(south_west, north_east)
    metric_dist = 2 * pi * radius * EARTH_RADIUS / 360

    filters = [CyclingFeature.geometry.intersects(
        functions.ST_MakeEnvelope(*bounds)
    )]

    if metric_dist >= 20000:
        filters.append(
            functions.ST_Length(
                CyclingFeature.geometry.cast(Geography)
            ) > min(metric_dist / 200, 1500)
        )

    query = db.query(functions.ST_AsGeoJSON(CyclingFeature)).filter(
        *filters
    )

    return FeatureCollection(
        type="FeatureCollection",
        features=list(
            map(parse_feat, query.all())
        )
    )
