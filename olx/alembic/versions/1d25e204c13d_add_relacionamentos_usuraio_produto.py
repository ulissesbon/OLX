"""Add relacionamentos usuraio-produto

Revision ID: 1d25e204c13d
Revises: 1ad422956102
Create Date: 2024-11-18 14:14:16.277423

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d25e204c13d'
down_revision: Union[str, None] = '1ad422956102'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_usuario', 'usuario', ['usuario_id'], ['id'])

    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('senha')

    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_constraint('fk_usuario', type_='foreignkey')

    # ### end Alembic commands ###
