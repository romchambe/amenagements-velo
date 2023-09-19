import { LatLng, LatLngBounds } from "leaflet";

export class ExtendedLatLng extends LatLng {
  toTuple() {
    return [this.lat, this.lng];
  }
}

export function getFormattedBounds(bounds: LatLngBounds) {
  return {
    north_east: new ExtendedLatLng(
      bounds.getNorthEast().lng,
      bounds.getNorthEast().lat,
    ).toTuple(),
    south_west: new ExtendedLatLng(
      bounds.getSouthWest().lng,
      bounds.getSouthWest().lat,
    ).toTuple(),
  };
}
