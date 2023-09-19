from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row
from ..core.models import CyclingFeature
from geojson_pydantic import Feature
from geoalchemy2 import functions, Geography
import json
from shapely import Point, distance
from math import pi

EARTH_RADIUS = 6378137


def parse_feat(f: Row):
    return Feature(**json.loads(f[0]))


def get_features(db: Session, bounds: list[float]) -> list[Feature]:
    south_west = Point(bounds[0], bounds[1])
    north_east = Point(bounds[2], bounds[3])

    radius = distance(south_west, north_east)
    metric_dist = 2 * pi * radius * EARTH_RADIUS / 360

    filters = [CyclingFeature.geometry.intersects(
        functions.ST_MakeEnvelope(*bounds)
    )]

    if metric_dist >= 10000:
        filters.append(
            functions.ST_Length(
                CyclingFeature.geometry.cast(Geography)
            ) > metric_dist / 100
        )

    query = db.query(functions.ST_AsGeoJSON(CyclingFeature)).filter(
        *filters
    )

    return list(
        map(parse_feat, query.all())
    )
