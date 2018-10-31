"""empty message

Revision ID: bcf2045c4e06
Revises: fd9dff883afd
Create Date: 2018-10-28 10:47:16.732679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcf2045c4e06'
down_revision = 'fd9dff883afd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('field_team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('espn_code', sa.String(length=8), nullable=True),
    sa.Column('espn_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('espn_projections', sa.Column('player_id', sa.Integer(), nullable=False))
    op.add_column('espn_projections', sa.Column('player_name', sa.String(length=64), nullable=True))
    op.add_column('espn_projections', sa.Column('team_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'espn_projections', 'field_team', ['team_id'], ['id'])
    op.drop_column('espn_projections', 'team')
    op.drop_column('espn_projections', 'id')
    op.drop_column('espn_projections', 'player')
    op.add_column('shark_projections', sa.Column('player_name', sa.String(length=64), nullable=False))
    op.add_column('shark_projections', sa.Column('position', sa.String(length=8), nullable=True))
    op.add_column('shark_projections', sa.Column('team_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shark_projections', 'field_team', ['team_id'], ['id'])
    op.drop_column('shark_projections', 'team')
    op.drop_column('shark_projections', 'player')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shark_projections', sa.Column('player', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
    op.add_column('shark_projections', sa.Column('team', sa.VARCHAR(length=8), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'shark_projections', type_='foreignkey')
    op.drop_column('shark_projections', 'team_id')
    op.drop_column('shark_projections', 'position')
    op.drop_column('shark_projections', 'player_name')
    op.add_column('espn_projections', sa.Column('player', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('espn_projections', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('espn_projections', sa.Column('team', sa.VARCHAR(length=8), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'espn_projections', type_='foreignkey')
    op.drop_column('espn_projections', 'team_id')
    op.drop_column('espn_projections', 'player_name')
    op.drop_column('espn_projections', 'player_id')
    op.drop_table('field_team')
    # ### end Alembic commands ###