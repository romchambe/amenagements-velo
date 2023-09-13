import { useFeaturesContext } from "./CyclingFeaturesProvider";
import { Feature } from "./Feature";

export const FeaturePainter = () => {
  const { features } = useFeaturesContext();

  return (
    <>
      {features.map(({ geometry }) => (
        <Feature
          positions={geometry.coordinates.map(([lng, lat]) => ({ lat, lng }))}
        />
      ))}
    </>
  );
};
