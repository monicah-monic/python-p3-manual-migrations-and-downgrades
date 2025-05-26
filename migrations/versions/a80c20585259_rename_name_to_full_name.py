"""Rename name to full_name

Revision ID: a80c20585259
Revises: d3c053f90d37
Create Date: 2025-05-26 14:35:55.806279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a80c20585259'
down_revision = 'd3c053f90d37'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'name', new_column_name='full_name')
    pass


def downgrade():
    op.alter_column('students', 'full_name', new_column_name= 'name')

