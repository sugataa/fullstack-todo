"""empty message

Revision ID: 79d9e8a2e097
Revises: db446dc06fc3
Create Date: 2017-09-26 10:55:39.155973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79d9e8a2e097'
down_revision = 'db446dc06fc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('position', sa.Integer(), nullable=True))
    op.drop_column('todos', 'sort_order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('sort_order', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('todos', 'position')
    # ### end Alembic commands ###