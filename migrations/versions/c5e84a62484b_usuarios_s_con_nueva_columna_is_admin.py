"""usuarios s con nueva columna is admin

Revision ID: c5e84a62484b
Revises: 48bef398534a
Create Date: 2022-10-16 18:36:38.296976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5e84a62484b'
down_revision = '48bef398534a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###
