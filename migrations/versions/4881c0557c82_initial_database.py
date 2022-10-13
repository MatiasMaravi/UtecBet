"""Initial database

Revision ID: 4881c0557c82
Revises: 
Create Date: 2022-10-13 11:33:57.929734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4881c0557c82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('winrate', sa.Float(), nullable=False),
    sa.Column('coach', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('transacciones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('cash', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('cash', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('bets',
    sa.Column('posible_ganador', sa.String(), nullable=False),
    sa.Column('cuota', sa.Float(), nullable=False),
    sa.Column('resultado', sa.String(), nullable=False),
    sa.Column('monto_apuesta', sa.Integer(), nullable=False),
    sa.Column('M_codigo', sa.Integer(), nullable=False),
    sa.Column('C_transaccion', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['C_transaccion'], ['transacciones.id'], ),
    sa.PrimaryKeyConstraint('M_codigo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bets')
    op.drop_table('users')
    op.drop_table('transacciones')
    op.drop_table('teams')
    # ### end Alembic commands ###