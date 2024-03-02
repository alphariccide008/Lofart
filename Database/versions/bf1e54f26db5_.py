"""empty message

Revision ID: bf1e54f26db5
Revises: 
Create Date: 2023-10-04 10:50:31.811495

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf1e54f26db5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userupload', schema=None) as batch_op:
        batch_op.drop_constraint('userupload_ibfk_2', type_='foreignkey')
        batch_op.drop_column('uploadpt')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('userupload', schema=None) as batch_op:
        batch_op.add_column(sa.Column('uploadpt', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('userupload_ibfk_2', 'payment', ['uploadpt'], ['payment_id'])

    # ### end Alembic commands ###