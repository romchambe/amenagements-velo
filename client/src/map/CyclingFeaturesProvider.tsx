import { FC, createContext, useCallback, useEffect } from "react";
import { useMapEvents } from "react-leaflet";
import { useApi } from "../utils/api.hook";
import { HttpVerb } from "../utils/api";
import { getFormattedBounds } from "../utils/geo";
import * as qs from "qs";
import { Map } from "leaflet";

type Props = {
  children?: React.ReactNode;
};

interface Feature {
  id: string;
}

const FeaturesContext = createContext<{ features: Feature[] }>({
  features: [],
});

export const CyclingFeaturesProvider: FC<Props> = ({ children }) => {
  const { fetchApi, data } = useApi<Feature[]>(() => ({
    url: "/features/within_bounds",
    method: HttpVerb.GET,
  }));

  const map = useMapEvents({
    moveend: () => {
      loadFeatures(map);
    },
  });

  const loadFeatures = useCallback(
    (map: Map) => {
      const zoom = map.getZoom();

      if (zoom >= 14) {
        const params = getFormattedBounds(map.getBounds());
        console.log("fetch", params);
        fetchApi({
          config: {
            params,
            paramsSerializer: (params) =>
              qs.stringify(params, { arrayFormat: "repeat" }),
          },
        });
      }
    },
    [map],
  );

  useEffect(() => {
    loadFeatures(map);
  }, [map]);

  console.log("data", data);
  return (
    <FeaturesContext.Provider value={{ features: data || [] }}>
      {children}
    </FeaturesContext.Provider>
  );
};
