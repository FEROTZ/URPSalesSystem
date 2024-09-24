from sqlalchemy import Column, Integer, ForeignKey, Table
from app.database.database import Base

roles_permissions = Table('roles_permissions', Base.metadata,
                          Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True),
                          Column('permission_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)