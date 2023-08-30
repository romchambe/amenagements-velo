from sqlalchemy import Column, Integer, String, Date, Float, Boolean, Enum
from geoalchemy2 import Geometry
from sqlalchemy.orm import DeclarativeBase
from .enums import Regime, Acces, Amenagement, Sens, Statut, Revetement, Emplacement


class Base(DeclarativeBase):
    pass


class CyclingFeature(Base):
    __tablename__ = "cycling_features"
    id = Column(Integer, primary_key=True, index=True)
    geometry = Column(Geometry(srid=4326), nullable=False)
    id_osm = Column(Integer, nullable=False)
    id_local = Column(String, nullable=False)
    code_com_g = Column(String, nullable=True)
    code_com_d = Column(String, nullable=True)
    ame_g = Column(Enum(Amenagement), nullable=True)
    ame_d = Column(Enum(Amenagement), nullable=True)
    regime_g = Column(Enum(Regime), nullable=True)
    regime_d = Column(Enum(Regime), nullable=True)
    sens_g = Column(Enum(Sens), nullable=True)
    sens_d = Column(Enum(Sens), nullable=True)
    statut_g = Column(Enum(Statut), nullable=True)
    statut_d = Column(Enum(Statut), nullable=True)
    revet_g = Column(Enum(Revetement), nullable=True)
    revet_d = Column(Enum(Revetement), nullable=True)
    date_maj = Column(Date, nullable=True)
    source = Column(String, nullable=False)
    project_c = Column(Integer, nullable=False)
    ref_geo = Column(String, nullable=False)
    access_ame = Column(Enum(Acces), nullable=True)
    trafic_vit = Column(Float, nullable=True)
    local_g = Column(Enum(Emplacement), nullable=True)
    local_d = Column(Enum(Emplacement), nullable=True)
    lumiere = Column(Boolean, nullable=True)
    num_iti = Column(String, nullable=True)
    largeur_g = Column(Float, nullable=True)
    largeur_d = Column(Float, nullable=True)
    d_service = Column(String, nullable=True)

# Schema des aménagements cyclables
# https://schema.data.gouv.fr/schemas/etalab/schema-amenagements-cyclables/0.3.4/schema_amenagements_cyclables.json


class CyclingFeatureRevision(Base):
    __tablename__ = "cycling_features_revisions"
    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(String, nullable=False)
    url = Column(String, nullable=False)
    date_refreshed = Column(Date, nullable=False)
