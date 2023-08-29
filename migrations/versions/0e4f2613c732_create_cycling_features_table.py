"""Create cycling features table

Revision ID: 0e4f2613c732
Revises: 
Create Date: 2023-08-29 13:27:19.898472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision: str = '0e4f2613c732'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_geospatial_table(
        'cycling_features',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('geometry', Geometry(srid=4326, spatial_index=False,
                                       from_text='ST_GeomFromEWKT', name='geometry', nullable=False), nullable=False),
        sa.Column('id_osm', sa.Integer(),
                  nullable=False),
        sa.Column('id_local', sa.String(),
                  nullable=False),
        sa.Column('code_com_g', sa.String(),
                  nullable=True),
        sa.Column('code_com_d', sa.String(),
                  nullable=True),
        sa.Column('ame_g', sa.Enum('PISTE CYCLABLE', 'BANDE CYCLABLE', 'DOUBLE SENS CYCLABLE PISTE', 'DOUBLE SENS CYCLABLE BANDE', 'DOUBLE SENS CYCLABLE NON MATERIALISE', 'VOIE VERTE', 'VELO RUE', 'COULOIR BUS+VELO',
                                   'RAMPE', 'GOULOTTE', 'AMENAGEMENT MIXTE PIETON VELO HORS VOIE VERTE', 'CHAUSSEE A VOIE CENTRALE BANALISEE', 'ACCOTEMENT REVETU HORS CVCB', 'AUCUN', 'AUTRE', name='amenagement'), nullable=True),
        sa.Column('ame_d', sa.Enum('PISTE CYCLABLE', 'BANDE CYCLABLE', 'DOUBLE SENS CYCLABLE PISTE', 'DOUBLE SENS CYCLABLE BANDE', 'DOUBLE SENS CYCLABLE NON MATERIALISE', 'VOIE VERTE', 'VELO RUE', 'COULOIR BUS+VELO',
                                   'RAMPE', 'GOULOTTE', 'AMENAGEMENT MIXTE PIETON VELO HORS VOIE VERTE', 'CHAUSSEE A VOIE CENTRALE BANALISEE', 'ACCOTEMENT REVETU HORS CVCB', 'AUCUN', 'AUTRE', name='amenagement'), nullable=True),
        sa.Column('regime_g', sa.Enum('ZONE 30', 'AIRE PIETONNE', 'ZONE DE RENCONTRE',
                                      'EN AGGLOMERATION', 'HORS AGGLOMERATION', 'AUTRE', name='regime'), nullable=True),
        sa.Column('regime_d', sa.Enum('ZONE 30', 'AIRE PIETONNE', 'ZONE DE RENCONTRE',
                                      'EN AGGLOMERATION', 'HORS AGGLOMERATION', 'AUTRE', name='regime'), nullable=True),
        sa.Column('sens_g', sa.Enum('UNIDIRECTIONNEL',
                                    'BIDIRECTIONNEL', name='sens'), nullable=True),
        sa.Column('sens_d', sa.Enum('UNIDIRECTIONNEL',
                                    'BIDIRECTIONNEL', name='sens'), nullable=True),
        sa.Column('statut_g', sa.Enum('EN TRAVAUX', 'EN SERVICE',
                                      'PROVISOIRE', name='statut'), nullable=True),
        sa.Column('statut_d', sa.Enum('EN TRAVAUX', 'EN SERVICE',
                                      'PROVISOIRE', name='statut'), nullable=True),
        sa.Column('revet_g', sa.Enum('LISSE', 'RUGUEUX',
                                     'MEUBLE', name='revetement'), nullable=True),
        sa.Column('revet_d', sa.Enum('LISSE', 'RUGUEUX',
                                     'MEUBLE', name='revetement'), nullable=True),
        sa.Column('date_maj', sa.Date(), nullable=True),
        sa.Column('source', sa.String(),
                  nullable=False),
        sa.Column('project_c', sa.Integer(),
                  nullable=False),
        sa.Column('ref_geo', sa.String(),
                  nullable=False),
        sa.Column('access_ame', sa.Enum('ROLLER', 'VELO DE ROUTE',
                                        'VTC', 'VTT', name='acces'), nullable=True),
        sa.Column('trafic_vit', sa.Float(),
                  nullable=True),
        sa.Column('local_g', sa.Enum('TROTTOIR', 'INTERMEDIAIRE',
                                     'CHAUSSEE', name='emplacement'), nullable=True),
        sa.Column('local_d', sa.Enum('TROTTOIR', 'INTERMEDIAIRE',
                                     'CHAUSSEE', name='emplacement'), nullable=True),
        sa.Column('lumiere', sa.Boolean(),
                  nullable=True),
        sa.Column('num_iti', sa.String(),
                  nullable=True),
        sa.Column('largeur_g', sa.Float(),
                  nullable=True),
        sa.Column('largeur_d', sa.Float(),
                  nullable=True),
        sa.Column('d_service', sa.String(),
                  nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_geospatial_index('idx_cycling_features_geometry', 'cycling_features', [
                               'geometry'], unique=False, postgresql_using='gist', postgresql_ops={})
    op.create_index(op.f('ix_cycling_features_id'),
                    'cycling_features', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_cycling_features_id'),
                  table_name='cycling_features')
    op.drop_geospatial_index('idx_cycling_features_geometry',
                             table_name='cycling_features', postgresql_using='gist', column_name='geometry')
    op.drop_table('cycling_features')
