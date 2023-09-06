import { MapContainer, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { CyclingFeaturesProvider } from "./CyclingFeaturesProvider";

export function Map() {
  return (
    <MapContainer
      center={[43.4945, -1.4737]}
      zoom={14}
      minZoom={13}
      style={{ width: "100%", height: "100%" }}
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://api.mapbox.com/styles/v1/romchambe/cllzce7wl00op01pfaky9hw90/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoicm9tY2hhbWJlIiwiYSI6ImNraG42MnNmODA5Ymoyd2s4bGtocnR6MWcifQ.BUHBlSsIxk8pGk12tnqSUQ"
      />
      <CyclingFeaturesProvider />
    </MapContainer>
  );
}
