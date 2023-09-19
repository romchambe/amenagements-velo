import { AxiosError, AxiosRequestConfig, AxiosResponse } from "axios";
import { Reducer, useCallback, useReducer } from "react";
import { api, HttpVerb } from "./api";

interface FetchApiState<T> {
  data: T | null;
  loading: boolean;
  error: NestException | Error | null;
}

export interface NestException {
  description: string[];
  message: string;
  statusCode: number;
  time: string;
}

export interface Endpoint {
  url: string;
  method: HttpVerb;
}

export type GetEndpointFunc = (param?: string | number) => Endpoint;

type FetchApiHook = <T, P = {}>(
  endpoint: GetEndpointFunc,
) => FetchApiState<T> & { fetchApi: FetchApiCallback<T, P> };
type FetchReducerAction<T> = { type: ACTIONS } & Partial<FetchApiState<T>>;

export type FetchApiCallback<D, P> = (args: {
  param?: string | number;
  payload?: P;
  config?: AxiosRequestConfig<P>;
}) => Promise<D | void>;

const INITIAL_STATE: FetchApiState<never> = {
  error: null,
  loading: false,
  data: null,
};

enum ACTIONS {
  FETCHED,
  FETCHING,
  ERROR,
}

const reducer = <T>(
  prevState: FetchApiState<T>,
  { type, ...nextState }: FetchReducerAction<T>,
): FetchApiState<T> => {
  switch (type) {
    case ACTIONS.FETCHING:
      return { ...prevState, loading: true };
    case ACTIONS.FETCHED:
      return {
        ...prevState,
        ...nextState,
        loading: false,
      };
    case ACTIONS.ERROR:
      return {
        ...prevState,
        error: nextState.error || null,
        loading: false,
      };
    default:
      return prevState;
  }
};

export const useApi: FetchApiHook = <D, P>(endpoint: GetEndpointFunc) => {
  const [state, dispatch] = useReducer<
    Reducer<FetchApiState<D>, FetchReducerAction<D>>
  >(reducer, INITIAL_STATE);

  const fetchApi = useCallback<FetchApiCallback<D, P>>(
    async ({ param, payload, config }) => {
      const { method, url } = endpoint(param);

      dispatch({ type: ACTIONS.FETCHING });

      return api
        .request<D, AxiosResponse<D>, P>({
          url,
          method,
          data: payload,
          ...config,
        })
        .then(({ data }) => {
          dispatch({ type: ACTIONS.FETCHED, data });
          return data;
        })
        .catch(({ response }: AxiosError<NestException>) => {
          const error =
            response?.data || new Error("Une erreur inconnue s'est produite");

          dispatch({ type: ACTIONS.ERROR, error });
        });
    },
    [endpoint],
  );

  return { ...state, fetchApi };
};
