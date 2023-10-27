import { LatLngExpression } from "leaflet";
import { Polyline, Popup } from "react-leaflet";
import { InternalFeatureProperties } from "./feature.type";
import { memo, useState } from "react";
import { useFeaturesContext } from "./CyclingFeaturesProvider";

interface FeatureProps {
  positions: LatLngExpression[];
  properties: InternalFeatureProperties;
}

const getLineWeight = (zoom: number) => {
  if (zoom <= 11) {
    return 1;
  }
  if (zoom <= 12) {
    return 1.5;
  }
  if (zoom <= 13) {
    return 2;
  }

  if (zoom <= 15) {
    return 3;
  }

  if (zoom <= 16) {
    return 3.5;
  } else return 4;
};

export const Feature = memo(({ positions, properties }: FeatureProps) => {
  const [hovered, setHovered] = useState(false);
  const { zoomLevel } = useFeaturesContext();

  return (
    <Polyline
      positions={positions}
      pathOptions={{
        color: hovered ? "yellow" : "#00F57E",
        weight: getLineWeight(zoomLevel),
      }}
      eventHandlers={{
        mouseover: () => {
          setHovered(true);
        },
        mouseout: () => {
          setHovered(false);
        },
      }}
    >
      <Popup>{JSON.stringify(properties)}</Popup>
    </Polyline>
  );
});
