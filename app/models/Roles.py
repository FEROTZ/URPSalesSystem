from sqlalchemy import Column, Integer, String, Enum, DateTime, exc
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from ..database import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)
    status = Column(Enum('active', 'inactive', name="role_status_type"), default='active')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime, nullable=True)

    permissions = relationship('Permission', secondary='roles_permissions', back_populates='roles')
    users = relationship('User', back_populates='role')

    def __repr__(self):
        return f"<Role(id={self.id}, name='{self.name}')>"

    def save(db:Session, **kwargs):
        try:
            role = Role(**kwargs)
            db.add(role)
            db.commit()
            db.refresh(role)
            return role
        except Exception as error:
            print(error)
            return {}

    def find(db: Session):
        try:
            return db.query(Role).filter_by(status = 'active').all()
        except Exception as error:
            print(error)
            return {}

    def find_one(db: Session, **kwargs):
        try:
            return db.query(Role).filter_by(**kwargs).first()
        except Exception as error:
            print(error)
            return {}

    def update(db: Session, role_id: int, **body):
        try:
            update_role = (
                db.query(Role)
                .filter_by(
                    id = role_id,
                    status = 'active'
                )
                .update(body, synchronize_session="fetch")
            )
            db.commit()

            return update_role
        except Exception as error:
            print(error)
            db.rollback()
            return {}

    def delete(db: Session, **kwargs):
        try:
            delete_user = (
                db.query(Role)
                .filter_by(
                    id = kwargs['id'],
                    status = "active"
                )
                .update({
                    "status" : "inactive",
                    "deleted_at" : datetime.now()
                }, synchronize_session="fetch")
            )
            db.commit(delete_user)
            return delete_user
        except exc.SQLAlchemyError as error:
            print(error)
            db.rollback()
            return {}