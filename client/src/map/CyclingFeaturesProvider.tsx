import {
  FC,
  createContext,
  memo,
  useCallback,
  useContext,
  useEffect,
  useState,
} from "react";
import { useMapEvents } from "react-leaflet";
import { useApi } from "../utils/api.hook";
import { HttpVerb, WithToken } from "../utils/api";
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
  const [token, setToken] = useState<string | null>(null);
  const [features, setFeatures] = useState<
    Feature<InternalFeatureProperties>[]
  >([]);

  const { fetchApi, loading, data } = useApi<
    WithToken & { collection: FeatureCollection<InternalFeatureProperties> }
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
      const headers = token
        ? {
            "X-Client-Token": token,
          }
        : {};

      fetchApi({
        config: {
          headers,
          params,
          paramsSerializer: (params: any) =>
            qs.stringify(params, { arrayFormat: "repeat" }),
        },
      });
    },
    [map, token],
  );

  useEffect(() => {
    if (!loading) {
      loadFeatures(map);
    }
  }, []);

  useEffect(() => {
    if (data?.client_token && data.client_token !== token) {
      setToken(data.client_token);
    }

    if (data?.collection.features) {
      setFeatures((prevFeatures) => [
        ...prevFeatures,
        ...data?.collection.features,
      ]);
    }
  }, [data]);

  return (
    <FeaturesContext.Provider value={{ features }}>
      <FeaturePainter />
    </FeaturesContext.Provider>
  );
});
