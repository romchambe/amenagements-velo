"""Create cycling feature revision

Revision ID: d9f75dccf9c4
Revises: 0e4f2613c732
Create Date: 2023-08-30 08:38:45.048423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9f75dccf9c4'
down_revision: Union[str, None] = '0e4f2613c732'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'cycling_features_revisions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('external_id', sa.String(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('date_refreshed', sa.Date(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_cycling_features_revisions_id'),
        'cycling_features_revisions',
        ['id'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_cycling_features_revisions_id'),
        table_name='cycling_features_revisions'
    )
    op.drop_table('cycling_features_revisions')
