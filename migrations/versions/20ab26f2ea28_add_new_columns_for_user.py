"""add new columns for user

Revision ID: 20ab26f2ea28
Revises: 511d79be72fb
Create Date: 2020-06-04 18:37:00.434674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20ab26f2ea28'
down_revision = '511d79be72fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_time')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###