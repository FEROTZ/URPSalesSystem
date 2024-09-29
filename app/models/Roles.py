# from sqlalchemy import Column, Integer, String, Enum, DateTime
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from ..database import Base

# class Role(Base):
#     __tablename__ = 'roles'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True, nullable=False)
#     description = Column(String)
#     status = Column(Enum('active', 'inactive', name="role_status_type"), default='active')
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

#     permissions = relationship('Permission', secondary='roles_permissions', back_populates='roles')
#     users = relationship('User', back_populates='role')

#     def __repr__(self):
#         return f"<Role(id={self.id}, name='{self.name}')>"