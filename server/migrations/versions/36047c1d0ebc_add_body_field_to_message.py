"""Add body field to Message

Revision ID: 36047c1d0ebc
Revises: 4c9adc16935c
Create Date: 2024-10-04 08:34:18.779807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36047c1d0ebc'
down_revision = '4c9adc16935c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('body', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'body')
    # ### end Alembic commands ###
