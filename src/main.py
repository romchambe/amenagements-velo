from fastapi import FastAPI, Depends
from .cycling_features.refresh_features import refresh_features
from sqlalchemy.orm import Session
from .core.database import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/refresh_cycling_features")
def refresh_cycling_features(db: Session = Depends(get_db)):
    refresh_features(db)
