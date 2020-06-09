"""empty message

Revision ID: 2be134af513e
Revises: 8127921f802f
Create Date: 2020-06-13 15:10:42.292688

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2be134af513e'
down_revision = '8127921f802f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('layers_json_url', sa.String(length=45), nullable=True))
    op.add_column('model', sa.Column('preprocessing_steps_json_url', sa.String(length=45), nullable=True))
    op.drop_column('model', 'preprocessing_steps_jon_url')
    op.drop_column('model', 'layers_jon_url')
    op.drop_column('model_has_label', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model_has_label', sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('model', sa.Column('layers_jon_url', mysql.VARCHAR(length=45), nullable=True))
    op.add_column('model', sa.Column('preprocessing_steps_jon_url', mysql.VARCHAR(length=45), nullable=True))
    op.drop_column('model', 'preprocessing_steps_json_url')
    op.drop_column('model', 'layers_json_url')
    # ### end Alembic commands ###
