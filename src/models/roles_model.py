from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc
from sqlalchemy.orm import relationship

from uuid import uuid4
from ..db import db, session
from datetime import datetime

class Roles(db):
    __tablename__ = "roles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    name = Column(String(80), nullable=False)
    createAt = Column(DateTime, default=datetime.now)
    updateAt = Column(DateTime)
    deleteAt = Column(DateTime)
    active = Column(Boolean, default=True)

class Roles_repository:
    async def save(self, **role: dict):
        try:
            new_role = Roles(**role)
            session.add(new_role)
            session.commit()
            return new_role
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}

    async def find(self, **role: dict):
        try:
            return session.query(Roles).filter_by(**role).all()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def find_one(self, **role: dict):
        try:
            return session.query(Roles).filter_by(**role).first()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def update(self, **role: dict):
        try:
            role["updateAt"] = datetime.now()
            update = (
                session.query(Roles)
                .filter_by(id = role["id"])
                .update(role, synchronize_session="fetch")
            )
            session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}