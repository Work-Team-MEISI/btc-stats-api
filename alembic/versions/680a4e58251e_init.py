"""init

Revision ID: 680a4e58251e
Revises: 
Create Date: 2021-11-10 12:20:27.919879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '680a4e58251e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('lower', sa.Float, nullable=False),
        sa.Column('higher', sa.Float, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('volume', sa.Float, nullable=False),
        sa.Column('change', sa.Float, nullable=True),
        sa.Column('timestamp', sa.DateTime, nullable=False),
    )

    op.create_table(
        'weekly_stats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('lower', sa.Float, nullable=False),
        sa.Column('higher', sa.Float, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('avg_volume', sa.Float, nullable=False),
        sa.Column('change', sa.Float, nullable=True),
        sa.Column('timestamp', sa.DateTime, nullable=False),
    )
    
    op.create_table(
        'monthly_stats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('lower', sa.Float, nullable=False),
        sa.Column('higher', sa.Float, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('avg_volume', sa.Float, nullable=False),
        sa.Column('change', sa.Float, nullable=True),
        sa.Column('timestamp', sa.DateTime, nullable=False),
    )
    
    op.create_table(
        'anual_stats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('lower', sa.Float, nullable=False),
        sa.Column('higher', sa.Float, nullable=False),
        sa.Column('open', sa.Float, nullable=False),
        sa.Column('close', sa.Float, nullable=False),
        sa.Column('avg_volume', sa.Float, nullable=False),
        sa.Column('change', sa.Float, nullable=True),
        sa.Column('timestamp', sa.DateTime, nullable=False),
    )



def downgrade():
    op.drop_table('stats')
    op.drop_table('weekly_stats')
    op.drop_table('monthly_stats')
    op.drop_table('anual_stats')
