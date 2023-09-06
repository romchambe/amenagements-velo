from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row
from ..core.models import CyclingFeature
from geojson_pydantic import Feature
from geoalchemy2 import functions
import json


def parse_f(f: Row):
    return Feature(**json.loads(f[0]))


def get_features(db: Session, bounds) -> list[Feature]:
    return list(
        map(parse_f,
            db.query(functions.ST_AsGeoJSON(CyclingFeature)).filter(
                CyclingFeature.geometry.intersects(
                    functions.ST_MakeEnvelope(*bounds)
                )
            ).all()))
