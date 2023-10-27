
from ..core.database import engine
from pathlib import Path
from geojsplit import geojsplit
from geopandas import GeoDataFrame
from .fetch_latest_version import check_latest_version, download_latest_version
from .features_revisions_queries import get_revision_by_external_id, create_revision
from sqlalchemy.orm import Session


def refresh_internal_data() -> int:
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

    return rows_count


def refresh_features(db: Session):
    version = check_latest_version()
    revision = get_revision_by_external_id(db, version.external_id)

    if (revision is None):
        download_latest_version(version.url)
        count = refresh_internal_data()
        create_revision(db, version)
        return f"Added {count} records to db"

    return "Database is up to date"
