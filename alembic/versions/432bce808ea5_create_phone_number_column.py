"""create phone number column

Revision ID: 432bce808ea5
Revises: 
Create Date: 2022-09-26 18:01:42.316696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '432bce808ea5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), unique=True))

def downgrade() -> None:
    op.drop_column('users', 'phone_number')
