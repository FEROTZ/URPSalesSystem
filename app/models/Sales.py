from sqlalchemy import Column, Integer, String, Numeric, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from datetime import datetime

class Sale(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_name = Column(String)
    quantity = Column(Integer)
    price = Column(Numeric(10, 2))
    total_price = Column(Numeric(10, 2))
    sale_date = Column(DateTime)
    status = Column(Enum('pending', 'completed', name='sale_status_type'), default='pending')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('User', back_populates='sales')
    
    def __repr__(self):
        return f"<Sale(id={self.id}, user_id={self.user_id}, product_name='{self.product_name}', total_price={self.total_price})>"