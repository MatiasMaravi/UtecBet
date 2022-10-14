"""clases con una relacion User-Bet

Revision ID: 013700a9977d
Revises: 17f3df8f0072
Create Date: 2022-10-14 11:06:07.368874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '013700a9977d'
down_revision = '17f3df8f0072'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bets', sa.Column('id_user', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'bets', 'users', ['id_user'], ['id'])
    op.add_column('matches', sa.Column('visit', sa.String(), nullable=False))
    op.add_column('matches', sa.Column('local', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('matches', 'local')
    op.drop_column('matches', 'visit')
    op.drop_constraint(None, 'bets', type_='foreignkey')
    op.drop_column('bets', 'id_user')
    # ### end Alembic commands ###
