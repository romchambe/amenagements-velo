import axios from "axios";

export enum HttpVerb {
  GET = "get",
  POST = "post",
  PUT = "put",
  PATCH = "patch",
}

const DEV_API_BASE_URL = "http://localhost:8000";

export const getApiBaseUrl = () => DEV_API_BASE_URL;

axios.defaults.baseURL = getApiBaseUrl();

export const api = axios;
