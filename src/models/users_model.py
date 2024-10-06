from sqlalchemy import Column, String, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc
from sqlalchemy.orm import relationship

from uuid import uuid4
from ..db import db, session
from datetime import datetime

class Users(db):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    id_role = Column(UUID(as_uuid=True), ForeignKey("roles.id"))
    createAt = Column(DateTime, default=datetime.now)
    updateAt = Column(DateTime)
    deleteAt = Column(DateTime)
    active = Column(Boolean, default=True)

    roles = relationship("Roles", back_populates="users")

class Users_repository:
    async def save(self, **user: dict):
        try:
            new_user = Users(**user)
            session.add(new_user)
            session.commit()
            return new_user
        except Exception as err:
            print(str(err))
            session.rollback()
            return {}

    async def find(self, **user: dict):
        try:
            return session.query(Users).filter_by(**user).all()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def find_one(self, **user: dict):
        try:
            return session.query(Users).filter_by(**user).first()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def update(self, **user: dict):
        try:
            user["updateAt"] = datetime.now()
            update = (
                session.query(Users)
                .filter_by(id = user["id"])
                .update(user, synchronize_session="fetch")
            )
            session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}