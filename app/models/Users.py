from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    status = Column(Enum('active', 'inactive', name='user_status_type'), default='active')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    role = relationship("Role", back_populates='users')
    sales = relationship("Sale", back_populates="user")
    
    @property
    def role_name(self):
        return self.role.name
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"