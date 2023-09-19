from fastapi import FastAPI, Depends, Query
from .cycling_features.refresh_features import refresh_features
from .cycling_features.get_features import get_features
from sqlalchemy.orm import Session
from .core.database import get_db
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from geojson_pydantic import FeatureCollection

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/refresh_cycling_features")
def refresh_cycling_features(db: Session = Depends(get_db)):
    refresh_features(db)


@app.get("/features/within_bounds")
def get_features_within_bounds(
    north_east: Annotated[list[float], Query()],
    south_west: Annotated[list[float], Query()],
    db: Session = Depends(get_db)
) -> FeatureCollection:
    features = get_features(
        db, [south_west[0], south_west[1], north_east[0], north_east[1]]
    )

    return FeatureCollection(type="FeatureCollection", features=features)
