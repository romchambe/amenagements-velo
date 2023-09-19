import { LatLngExpression } from "leaflet";
import { Polyline } from "react-leaflet";

interface FeatureProps {
  id: number;
  positions: LatLngExpression[];
}

export const Feature = ({ positions }: FeatureProps) => {
  return (
    <Polyline
      key={"toto"}
      positions={positions}
      pathOptions={{ color: "#5CFFB0" }}
    />
  );
};
