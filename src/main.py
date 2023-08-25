from fastapi import FastAPI
import geopandas
from geojsplit import geojsplit
from pathlib import Path



app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/split")
def read_dep():
    geojson = geojsplit.GeoJSONBatchStreamer(Path().joinpath("src", "data", "amenagements.geojson"))
    
    first_set = next(geojson.stream(batch=2))
    print(first_set)
    
    
