from sqlalchemy import Column, ForeignKey, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc

from uuid import uuid4
from ..db import db, session
from datetime import datetime

class UsersPartners(db):
    __tablename__ = "users_partners"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    id_user = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    id_partner = Column(UUID(as_uuid=True), ForeignKey("partners.id"))
    createAt = Column(DateTime, default=datetime.now)
    updateAt = Column(DateTime)
    deleteAt = Column(DateTime)
    active = Column(Boolean, default=True)

class UsersPartners_repository:
    async def save(self, **user_partner: dict):
        try:
            new_user_partner = UsersPartners(**user_partner)
            session.add(new_user_partner)
            session.commit()
            return new_user_partner
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}

    async def find(self, **user_partner: dict):
        try:
            return session.query(UsersPartners).filter_by(**user_partner).all()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def find_one(self, **user_partner: dict):
        try:
            return session.query(UsersPartners).filter_by(**user_partner).first()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def update(self, **user_partner: dict):
        try:
            user_partner["updateAt"] = datetime.now()
            update = (
                session.query(UsersPartners)
                .filter_by(id = user_partner["id"])
                .update(user_partner, synchronize_session="fetch")
            )
            session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}