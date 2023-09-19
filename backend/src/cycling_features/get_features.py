from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row
from ..core.models import CyclingFeature
from geojson_pydantic import Feature
from geoalchemy2 import functions, Geography
import json


def parse_feat(f: Row):
    return Feature(**json.loads(f[0]))


def get_features(db: Session, bounds: list[float], zoom: int) -> list[Feature]:
    filters = [CyclingFeature.geometry.intersects(
        functions.ST_MakeEnvelope(*bounds)
    )]

    if zoom <= 14:
        filters.append(
            functions.ST_Length(
                CyclingFeature.geometry.cast(Geography)
            ) > 500
        )

    query = db.query(functions.ST_AsGeoJSON(CyclingFeature)).filter(
        *filters
    )

    return list(
        map(parse_feat, query.all())
    )
