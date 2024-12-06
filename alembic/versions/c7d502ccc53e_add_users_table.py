"""add users table

Revision ID: c7d502ccc53e
Revises: 3851c8d0ba1a
Create Date: 2024-12-05 21:47:04.717577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'c7d502ccc53e'
down_revision: Union[str, None] = '3851c8d0ba1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userindb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_userindb_id'), 'userindb', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_userindb_id'), table_name='userindb')
    op.drop_table('userindb')
    # ### end Alembic commands ###