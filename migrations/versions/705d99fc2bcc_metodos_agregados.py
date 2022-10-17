"""metodos agregados

Revision ID: 705d99fc2bcc
Revises: 8629b52e541f
Create Date: 2022-10-14 07:56:12.986721

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '705d99fc2bcc'
down_revision = '8629b52e541f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('bets', sa.Column('monto_apuesta', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('bets', sa.Column('M_codigo', sa.INTEGER(), server_default=sa.text('nextval(\'"bets_M_codigo_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.add_column('bets', sa.Column('C_transaccion', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('bets', sa.Column('cuota', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.add_column('bets', sa.Column('posible_ganador', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('bets', sa.Column('resultado', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'bets', type_='foreignkey')
    op.drop_constraint(None, 'bets', type_='foreignkey')
    op.create_foreign_key('bets_C_transaccion_fkey', 'bets', 'transacciones', ['C_transaccion'], ['id'])
    op.drop_column('bets', 'match_code')
    op.drop_column('bets', 'id_user')
    op.drop_column('bets', 'result')
    op.drop_column('bets', 'bet_amount')
    op.drop_column('bets', 'quota')
    op.drop_column('bets', 'id')
    op.drop_table('matches')
    # ### end Alembic commands ###
