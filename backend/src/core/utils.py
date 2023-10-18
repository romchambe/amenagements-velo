from shapely.geometry import Polygon


def get_polygon_from_ne_sw(bounds: list[float]) -> Polygon:
    south_west = [bounds[0], bounds[1]]
    north_east = [bounds[2], bounds[3]]
    north_west = [bounds[0], bounds[3]]
    south_east = [bounds[2], bounds[1]]

    return Polygon([south_west, north_west, north_east, south_east])
