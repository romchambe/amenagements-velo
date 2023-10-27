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
  zoomLevel: number;
}>({
  features: [],
  zoomLevel: 13,
});

export const useFeaturesContext = () => useContext(FeaturesContext);

export const CyclingFeaturesProvider: FC<Props> = memo(() => {
  const [token, setToken] = useState<string | null>(null);
  const [zoomLevel, setZoomLevel] = useState(13);

  const [features, setFeatures] = useState<
    Record<number, Feature<InternalFeatureProperties>>
  >({});

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

    zoomend: ({ target }) => {
      if (zoomLevel !== target._zoom) {
        console.log(target._zoom);
        setZoomLevel(target._zoom);
      }
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
      const nextFeatures = data?.collection.features;

      setFeatures((prevFeaturesStore) => {
        const nextFeaturesStore = nextFeatures.reduce<
          Record<number, Feature<InternalFeatureProperties>>
        >((store, feature) => {
          store[feature.properties.id] = feature;

          return store;
        }, {});

        return { ...prevFeaturesStore, ...nextFeaturesStore };
      });
    }
  }, [data]);

  return (
    <FeaturesContext.Provider
      value={{ features: Object.values(features), zoomLevel }}
    >
      <FeaturePainter />
    </FeaturesContext.Provider>
  );
});
