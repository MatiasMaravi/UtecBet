"""Second database

Revision ID: 8629b52e541f
Revises: 4881c0557c82
Create Date: 2022-10-13 11:36:43.050812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8629b52e541f'
down_revision = '4881c0557c82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
