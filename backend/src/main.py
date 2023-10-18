from fastapi import FastAPI, Depends, Query, Header
from .cycling_features.refresh_features import refresh_features
from .cycling_features.get_features import get_features, GetFeaturesResponse
from sqlalchemy.orm import Session
from .core.database import get_db
from .core.request import create_token, decode_token
from .core.cache import Cache
from .core.utils import get_polygon_from_ne_sw
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from dotenv import load_dotenv
from shapely.ops import unary_union


load_dotenv()

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"],
    allow_headers=['X-Client-Token']
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
    x_client_token:  Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db)
) -> GetFeaturesResponse:
    client_id = None
    client_token = x_client_token

    if client_token is None:
        client_id, client_token = create_token()
    else:
        client_id = decode_token(client_token)

    requested_polygon = get_polygon_from_ne_sw(
        [south_west[0], south_west[1], north_east[0], north_east[1]]
    )

    features_collection = get_features(
        db, requested_polygon, client_id
    )

    return GetFeaturesResponse(
        collection=features_collection,
        client_token=client_token
    )
