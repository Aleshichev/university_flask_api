"""empty message

Revision ID: 04988f8b9a44
Revises: 
Create Date: 2022-10-13 16:59:09.816948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04988f8b9a44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('groups',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('students',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('group_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_table('groups')
    op.drop_table('courses')
    # ### end Alembic commands ###
