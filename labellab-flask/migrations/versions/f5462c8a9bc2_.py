"""empty message

Revision ID: f5462c8a9bc2
Revises: 
Create Date: 2020-08-06 19:04:37.588131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5462c8a9bc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('revoked_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('thumbnail', sa.String(length=1500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=80), nullable=False),
    sa.Column('project_description', sa.String(length=128), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['user.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(length=128), nullable=False),
    sa.Column('image_url', sa.String(length=80), nullable=False),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('labelled', sa.Boolean(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label_name', sa.String(length=128), nullable=False),
    sa.Column('label_type', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('type', sa.String(length=45), nullable=False),
    sa.Column('source', sa.String(length=45), nullable=False),
    sa.Column('preprocessing_steps_json_url', sa.String(length=45), nullable=True),
    sa.Column('layers_json_url', sa.String(length=45), nullable=True),
    sa.Column('train', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.Column('test', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.Column('validation', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.Column('epochs', sa.Integer(), nullable=True),
    sa.Column('batch_size', sa.Integer(), nullable=True),
    sa.Column('learning_rate', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.Column('loss', sa.String(length=45), nullable=True),
    sa.Column('optimizer', sa.String(length=45), nullable=True),
    sa.Column('metric', sa.String(length=45), nullable=True),
    sa.Column('loss_graph_url', sa.String(length=45), nullable=True),
    sa.Column('accuracy_graph_url', sa.String(length=45), nullable=True),
    sa.Column('saved_model_url', sa.String(length=45), nullable=True),
    sa.Column('transfer_source', sa.String(length=45), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_name', sa.String(length=80), nullable=False),
    sa.Column('role', sa.String(length=128), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('labeldata',
    sa.Column('id', sa.String(length=45), nullable=False),
    sa.Column('months_passed', sa.Integer(), nullable=True),
    sa.Column('image_id', sa.Integer(), nullable=False),
    sa.Column('label_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('model_has_label',
    sa.Column('model_id', sa.Integer(), nullable=False),
    sa.Column('label_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.ForeignKeyConstraint(['model_id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('model_id', 'label_id')
    )
    op.create_table('projectmember',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['team.id'], onupdate='cascade', ondelete='cascade'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('point',
    sa.Column('id', sa.String(length=45), nullable=False),
    sa.Column('y_coordinate', sa.Float(), nullable=False),
    sa.Column('x_coordinate', sa.Float(), nullable=False),
    sa.Column('labeldata_id', sa.String(length=45), nullable=False),
    sa.ForeignKeyConstraint(['labeldata_id'], ['labeldata.id'], onupdate='cascade', ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=120), nullable=False),
    sa.Column('category', sa.String(length=20), nullable=False),
    sa.Column('entity_type', sa.String(length=10), nullable=True),
    sa.Column('entity_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('point')
    op.drop_table('projectmember')
    op.drop_table('model_has_label')
    op.drop_table('labeldata')
    op.drop_table('team')
    op.drop_table('model')
    op.drop_table('label')
    op.drop_table('image')
    op.drop_table('project')
    op.drop_table('user')
    op.drop_table('revoked_token')
    op.drop_table('log')
    # ### end Alembic commands ###
