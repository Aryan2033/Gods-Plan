"""add email column to users

Revision ID: 0002_add_email
Revises: 0001_create_users
Create Date: 2026-06-10
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002_add_email'
down_revision = '0001_create_users'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'email')
