type Regime =
  | "ZONE 30"
  | "AIRE PIETONNE"
  | "ZONE DE RENCONTRE"
  | "EN AGGLOMERATION"
  | "HORS AGGLOMERATION"
  | "AUTRE";

type Amenagement =
  | "PISTE CYCLABLE"
  | "BANDE CYCLABLE"
  | "DOUBLE_SENS_CYCLABLE_PISTE"
  | "DOUBLE SENS CYCLABLE BANDE"
  | "DOUBLE SENS CYCLABLE NON MATERIALISE"
  | "VOIE VERTE"
  | "VELO RUE"
  | "COULOIR BUS+VELO"
  | "RAMPE"
  | "GOULOTTE"
  | "AMENAGEMENT MIXTE PIETON VELO HORS VOIE VERTE"
  | "CHAUSSEE A VOIE CENTRALE BANALISEE"
  | "CHAUSSEE_A_VOIE_CENTRALE_BANALISEE"
  | "ACCOTEMENT REVETU HORS CVCB"
  | "AUCUN"
  | "AUTRE";

type Revetement = "LISSE" | "RUGUEUX" | "MEUBLE";

type Statut = "EN TRAVAUX" | "EN SERVICE" | "PROVISOIRE";

type Emplacement = "TROTTOIR" | "INTERMEDIAIRE" | "CHAUSSEE";

type Sens = "UNIDIRECTIONNEL" | "BIDIRECTIONNEL";

type Acces = "ROLLER" | "VELO DE ROUTE" | "VTC" | "VTT";

export interface Feature<T> {
  type: "Feature";
  geometry: { type: "LineString"; coordinates: [number, number][] };
  properties: T;
}

export interface FeatureCollection<T> {
  type: "FeatureCollection";
  features: Feature<T>[];
}

export interface InternalFeatureProperties {
  access_ame: Acces | null;
  ame_d: Amenagement | null;
  ame_g: Amenagement | null;
  code_com_d: string | null;
  code_com_g: string | null;
  d_service: string | null;
  date_maj: string;
  id: number;
  id_local: string;
  id_osm: number;
  largeur_d: number | null;
  largeur_g: number | null;
  local_d: Emplacement | null;
  local_g: Emplacement | null;
  lumiere: boolean | null;
  num_iti: string | null;
  project_c: 4326;
  ref_geo: "OpenStreetmap";
  regime_d: Regime | null;
  regime_g: Regime | null;
  revet_d: Revetement | null;
  revet_g: Revetement | null;
  sens_d: Sens | null;
  sens_g: Sens | null;
  source: string;
  statut_d: Statut | null;
  statut_g: Statut | null;
  trafic_vit: number | null;
}
