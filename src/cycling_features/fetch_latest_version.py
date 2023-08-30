import requests
import json
from dateutil import parser
from urllib.request import urlretrieve
from pathlib import Path

DATASET_ID = "60a37b7f303fdf4f2654b73d"


class OpenCyclingFeaturesVersion:
    def __init__(self, external_id: str, created_at: str, url: str):
        self.external_id = external_id
        self.created_at = created_at
        self.url = url


def check_latest_version() -> OpenCyclingFeaturesVersion:
    response = requests.get(
        f"https://www.data.gouv.fr/api/1/datasets/{DATASET_ID}",
        headers={"X-Fields": "resources"}
    )
    resources = json.loads(response.text)["resources"]

    latest_version = sorted(
        resources,
        key=lambda resource: parser.parse(
            resource['created_at']),
        reverse=True
    )[0]

    print(parser.parse(latest_version['created_at']))

    return OpenCyclingFeaturesVersion(
        external_id=latest_version['id'],
        url=latest_version['url'],
        created_at=latest_version['created_at'],
    )


def download_latest_version(url: str):
    urlretrieve(
        url,
        Path().joinpath("data", "amenagements.geojson")
    )
