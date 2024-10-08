"""add Department

Revision ID: 2edc48eb0227
Revises: 6fa241199665
Create Date: 2024-10-02 14:55:41.398128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2edc48eb0227'
down_revision = '6fa241199665'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
