import { FC } from "react";
import { useMapEvents } from "react-leaflet";

type Props = {
  children?: React.ReactNode;
};
export const CyclingFeaturesProvider: FC<Props> = ({ children }) => {
  const map = useMapEvents({
    moveend: () => {
      console.log(map.getBounds().getNorthEast());
    },
  });
  console.log(map);
  return children;
};
