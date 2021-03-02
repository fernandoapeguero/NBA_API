"""updated player model

Revision ID: d54747e62e04
Revises: 2fb1ed1e09c7
Create Date: 2021-03-02 12:56:48.581645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd54747e62e04'
down_revision = '2fb1ed1e09c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('player_number', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'players', ['player_number'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'players', type_='unique')
    op.drop_column('players', 'player_number')
    # ### end Alembic commands ###