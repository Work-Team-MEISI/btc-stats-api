"""Add SVMR Stats

Revision ID: 231b38345a65
Revises: 680a4e58251e
Create Date: 2022-02-01 22:22:36.527638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '231b38345a65'
down_revision = '680a4e58251e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'svmr_stats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('value', sa.Float, nullable=False),
        sa.Column('accuracy', sa.Float, nullable=False),
        sa.Column('date', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('svmr_stats')
