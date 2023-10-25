import { useFeaturesContext } from "./CyclingFeaturesProvider";
import { Feature } from "./Feature";

export const FeaturePainter = () => {
  const { features } = useFeaturesContext();

  return (
    <>
      {features.map(({ geometry, properties }) => {
        const { id } = properties;
        return (
          <Feature
            key={id}
            positions={geometry.coordinates.map(([lng, lat]) => ({ lat, lng }))}
            properties={properties}
          />
        );
      })}
    </>
  );
};
