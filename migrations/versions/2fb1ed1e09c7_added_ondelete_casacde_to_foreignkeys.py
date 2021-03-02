"""added ondelete casacde to foreignkeys

Revision ID: 2fb1ed1e09c7
Revises: 8468a07558bb
Create Date: 2021-03-02 00:15:35.380937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fb1ed1e09c7'
down_revision = '8468a07558bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('events_team_id_fkey', 'events', type_='foreignkey')
    op.drop_constraint('events_team_id_two_fkey', 'events', type_='foreignkey')
    op.drop_constraint('events_venue_id_fkey', 'events', type_='foreignkey')
    op.create_foreign_key(None, 'events', 'teams', ['team_id_two'], ['id'], ondelete='cascade')
    op.create_foreign_key(None, 'events', 'teams', ['team_id'], ['id'], ondelete='cascade')
    op.create_foreign_key(None, 'events', 'venues', ['venue_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.create_foreign_key('events_venue_id_fkey', 'events', 'venues', ['venue_id'], ['id'])
    op.create_foreign_key('events_team_id_two_fkey', 'events', 'teams', ['team_id_two'], ['id'])
    op.create_foreign_key('events_team_id_fkey', 'events', 'teams', ['team_id'], ['id'])
    # ### end Alembic commands ###
