import {
  FC,
  createContext,
  memo,
  useCallback,
  useContext,
  useEffect,
} from "react";
import { useMapEvents } from "react-leaflet";
import { useApi } from "../utils/api.hook";
import { HttpVerb } from "../utils/api";
import { getFormattedBounds } from "../utils/geo";
import * as qs from "qs";
import { Map } from "leaflet";
import { FeaturePainter } from "./FeaturePainter";
import {
  Feature,
  FeatureCollection,
  InternalFeatureProperties,
} from "./feature.type";

type Props = {
  children?: React.ReactNode;
};

const FeaturesContext = createContext<{
  features: Feature<InternalFeatureProperties>[];
}>({
  features: [],
});

export const useFeaturesContext = () => useContext(FeaturesContext);

export const CyclingFeaturesProvider: FC<Props> = memo(() => {
  const { fetchApi, data } = useApi<
    FeatureCollection<InternalFeatureProperties>
  >(() => ({
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
      const params = getFormattedBounds(map.getBounds());

      fetchApi({
        config: {
          params,
          paramsSerializer: (params) =>
            qs.stringify(params, { arrayFormat: "repeat" }),
        },
      });
    },
    [map],
  );

  useEffect(() => {
    loadFeatures(map);
  }, []);

  return (
    <FeaturesContext.Provider value={{ features: data?.features || [] }}>
      <FeaturePainter />
    </FeaturesContext.Provider>
  );
});
