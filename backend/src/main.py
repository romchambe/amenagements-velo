from fastapi import FastAPI, Depends, Query, Header
from .cycling_features.refresh_features import refresh_features
from .cycling_features.get_features import get_features, GetFeaturesResponse
from sqlalchemy.orm import Session
from .core.database import get_db
from .core.request import create_token, decode_token
from .core.cache import Cache
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
cache = Cache()

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
    request_token:  Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db)
) -> GetFeaturesResponse:
    id = None

    if request_token is None:
        id, request_token = create_token()
    else:
        id = decode_token(request_token)

    # Get uncached area boundaries
    print(id)

    features_collection = get_features(
        db, [south_west[0], south_west[1], north_east[0], north_east[1]]
    )

    return GetFeaturesResponse(
        features_collection=features_collection,
        request_token=request_token
    )
