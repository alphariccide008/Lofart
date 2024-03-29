"""empty message

Revision ID: 3be6168b1404
Revises: 
Create Date: 2024-03-02 04:03:32.708902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3be6168b1404'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adminreg',
    sa.Column('admin_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('admin_username', sa.String(length=20), nullable=False),
    sa.Column('admin_pwd', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_fname', sa.String(length=64), nullable=False),
    sa.Column('user_lname', sa.String(length=64), nullable=False),
    sa.Column('user_add', sa.String(length=200), nullable=False),
    sa.Column('user_city', sa.String(length=64), nullable=False),
    sa.Column('user_reg', sa.DateTime(), nullable=True),
    sa.Column('user_email', sa.String(length=100), nullable=False),
    sa.Column('user_phone', sa.String(length=50), nullable=False),
    sa.Column('user_profile', sa.String(length=300), nullable=True),
    sa.Column('user_pix', sa.String(length=120), nullable=True),
    sa.Column('user_username', sa.String(length=100), nullable=False),
    sa.Column('user_state', sa.String(length=100), nullable=True),
    sa.Column('user_lga', sa.String(length=100), nullable=True),
    sa.Column('user_password', sa.String(length=225), nullable=False),
    sa.Column('user_usertype', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_user_add'), ['user_add'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_city'), ['user_city'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_email'), ['user_email'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_fname'), ['user_fname'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_lga'), ['user_lga'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_lname'), ['user_lname'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_password'), ['user_password'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_phone'), ['user_phone'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_profile'), ['user_profile'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_state'), ['user_state'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_username'), ['user_username'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_user_usertype'), ['user_usertype'], unique=False)

    op.create_table('order',
    sa.Column('order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_amt', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('order_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_user_id'], ['user.user_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('order_id')
    )
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_order_order_amt'), ['order_amt'], unique=False)

    op.create_table('userupload',
    sa.Column('upload_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('upload_filename', sa.String(length=200), nullable=False),
    sa.Column('upload_desc', sa.String(length=500), nullable=False),
    sa.Column('upload_amt', sa.Integer(), nullable=False),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.Column('upload_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['upload_user_id'], ['user.user_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('upload_id')
    )
    with op.batch_alter_table('userupload', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_userupload_upload_amt'), ['upload_amt'], unique=False)
        batch_op.create_index(batch_op.f('ix_userupload_upload_desc'), ['upload_desc'], unique=False)
        batch_op.create_index(batch_op.f('ix_userupload_upload_filename'), ['upload_filename'], unique=False)

    op.create_table('payment',
    sa.Column('payment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('payment_status', sa.String(length=10), nullable=False),
    sa.Column('payment_amt', sa.Integer(), nullable=False),
    sa.Column('refno', sa.String(length=12), nullable=False),
    sa.Column('payment_date', sa.DateTime(), nullable=True),
    sa.Column('payment_user_id', sa.Integer(), nullable=True),
    sa.Column('payment_order_id', sa.Integer(), nullable=True),
    sa.Column('ptupload', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['payment_order_id'], ['order.order_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['payment_user_id'], ['user.user_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['ptupload'], ['userupload.upload_id'], ),
    sa.PrimaryKeyConstraint('payment_id')
    )
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_payment_payment_amt'), ['payment_amt'], unique=False)
        batch_op.create_index(batch_op.f('ix_payment_payment_status'), ['payment_status'], unique=False)
        batch_op.create_index(batch_op.f('ix_payment_refno'), ['refno'], unique=False)

    op.create_table('usercomment',
    sa.Column('usercomment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_comment', sa.String(length=300), nullable=True),
    sa.Column('comment_date', sa.DateTime(), nullable=True),
    sa.Column('comment_user_id', sa.Integer(), nullable=True),
    sa.Column('comment_upload_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_upload_id'], ['userupload.upload_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['comment_user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('usercomment_id')
    )
    with op.batch_alter_table('usercomment', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_usercomment_user_comment'), ['user_comment'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usercomment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_usercomment_user_comment'))

    op.drop_table('usercomment')
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_payment_refno'))
        batch_op.drop_index(batch_op.f('ix_payment_payment_status'))
        batch_op.drop_index(batch_op.f('ix_payment_payment_amt'))

    op.drop_table('payment')
    with op.batch_alter_table('userupload', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_userupload_upload_filename'))
        batch_op.drop_index(batch_op.f('ix_userupload_upload_desc'))
        batch_op.drop_index(batch_op.f('ix_userupload_upload_amt'))

    op.drop_table('userupload')
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_order_order_amt'))

    op.drop_table('order')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_user_usertype'))
        batch_op.drop_index(batch_op.f('ix_user_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_user_state'))
        batch_op.drop_index(batch_op.f('ix_user_user_profile'))
        batch_op.drop_index(batch_op.f('ix_user_user_phone'))
        batch_op.drop_index(batch_op.f('ix_user_user_password'))
        batch_op.drop_index(batch_op.f('ix_user_user_lname'))
        batch_op.drop_index(batch_op.f('ix_user_user_lga'))
        batch_op.drop_index(batch_op.f('ix_user_user_fname'))
        batch_op.drop_index(batch_op.f('ix_user_user_email'))
        batch_op.drop_index(batch_op.f('ix_user_user_city'))
        batch_op.drop_index(batch_op.f('ix_user_user_add'))

    op.drop_table('user')
    op.drop_table('adminreg')
    # ### end Alembic commands ###
