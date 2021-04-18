"""empty message

Revision ID: 443889ffc0cb
Revises: 234c17fafece
Create Date: 2021-04-17 21:05:31.584763

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '443889ffc0cb'
down_revision = '234c17fafece'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('user_id', sa.Integer(), nullable=True))
    op.alter_column('favorites', 'people_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'planets_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'vehicles_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'favorites', 'vehicles', ['vehicles_id'], ['id'])
    op.create_foreign_key(None, 'favorites', 'planets', ['planets_id'], ['id'])
    op.create_foreign_key(None, 'favorites', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'favorites', 'people', ['people_id'], ['id'])
    op.drop_column('favorites', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('user', mysql.VARCHAR(length=250), nullable=False))
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.alter_column('favorites', 'vehicles_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'planets_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'people_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('favorites', 'user_id')
    # ### end Alembic commands ###
