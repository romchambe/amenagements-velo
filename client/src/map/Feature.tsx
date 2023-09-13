import { LatLngExpression } from "leaflet";
import { Polyline } from "react-leaflet";

interface FeatureProps {
  positions: LatLngExpression[];
}

export const Feature = ({ positions }: FeatureProps) => {
  return <Polyline positions={positions} pathOptions={{ color: "#80ffdb" }} />;
};
