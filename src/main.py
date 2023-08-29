from fastapi import FastAPI
from geopandas import GeoDataFrame
from geojsplit import geojsplit
from pathlib import Path
from .core.database import engine

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/refresh_cycling_features")
def update_cycling_features():
    geojson = geojsplit.GeoJSONBatchStreamer(
        Path().joinpath("data", "amenagements.geojson")
    )

    rows_count = 0

    for features in geojson.stream(batch=100):
        dataframe = GeoDataFrame.from_features(features, crs='EPSG:4326')
        dataframe.reset_index()
        dataframe['id'] = dataframe.index + rows_count

        try:
            dataframe.to_postgis(
                name='cycling_features',
                con=engine,
                if_exists='append'
            )
        except:
            dataframe.to_csv(
                Path().joinpath(
                    'data',
                    f"failed_{rows_count}.csv"
                )
            )

        rows_count += len(dataframe.index)

    print('Count:', rows_count)
