from sqlalchemy import Column, Integer, String, Enum, DateTime, exc
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from ..database import Base

class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    status = Column(Enum('active', 'inactive', name="permission_status_type"), default='active')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    roles = relationship('Role', secondary='roles_permissions', back_populates='permissions')

    def save(db: Session, **kwargs):
        try:
            permission = Permission(**kwargs)
            db.add(permission)
            db.commit()
            db.refresh(permission)
            return permission
        except Exception as error:
            print(error)
            return {}

    def find(db: Session):
        try:
            return db.query(Permission).filter_by(status = 'active').all()
        except Exception as error:
            print(error)
            return {}

    def find_one(db: Session, **kwargs):
        try:
            return db.query(Permission).filter_by(**kwargs).first()
        except Exception as error:
            print(error)
            return {}

    def update(db: Session, permission_id: int, **body):
        try:
            update_permission = (
                db.query(Permission)
                .filter_by(
                    id = permission_id,
                    status = 'active'
                )
                .update(body, synchronize_session="fetch")
            )
            db.commit()

            return update_permission
        except Exception as error:
            print(error)
            db.rollback()
            return {}

    def delete(db: Session, **kwargs):
        try:
            delete_permission = (
                db.query(Permission)
                .filter_by(**kwargs)
                .update({
                    "status": "inactive",
                    "updated_at": datetime.now(),
                }, synchronize_session="fetch")
            )
            db.commit()
            return delete_permission
        except exc.SQLAlchemyError as error:
            print(error)
            db.rollback()
            return {}