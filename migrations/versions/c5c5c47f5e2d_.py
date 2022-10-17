"""empty message

Revision ID: c5c5c47f5e2d
Revises: e098c593d08c
Create Date: 2022-10-14 11:54:43.676129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5c5c47f5e2d'
down_revision = 'e098c593d08c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transacciones')
    op.add_column('bets', sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('matches', sa.Column('fecha_creacion', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.drop_constraint('matches_local_fkey', 'matches', type_='foreignkey')
    op.add_column('teams', sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('users', sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created_time')
    op.drop_column('teams', 'time_created')
    op.create_foreign_key('matches_local_fkey', 'matches', 'teams', ['local'], ['name'])
    op.drop_column('matches', 'fecha_creacion')
    op.drop_column('bets', 'created_time')
    op.create_table('transacciones',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('cash', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='transacciones_pkey')
    )
    # ### end Alembic commands ###
