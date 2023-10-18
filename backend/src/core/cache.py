from datetime import datetime, timedelta, timezone
from shapely.geometry import Polygon


class PolygonCacheItem:
    def __init__(self, id: int, data: Polygon):
        self.id = id
        self.polygon = data
        self.expiration = datetime.now(tz=timezone.utc) + timedelta(hours=1)


class Cache:
    def __init__(self):
        self.items: dict[int, PolygonCacheItem] = dict()
        self.current_id: int = 0

    def get_next_id(self) -> int:
        self.current_id += 1
        self.items[self.current_id] = None
        return self.current_id

    def upsert_polygon_item(self, id: int, polygon: Polygon):
        self.items[id] = PolygonCacheItem(id, polygon)

    def get_item(self, id: int) -> PolygonCacheItem | None:
        if self.items.keys().__contains__(id):
            return self.items[id]
        else:
            return None


cache = Cache()
