from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc

from uuid import uuid4
from ..db import db, session
from datetime import datetime

class Partners(db):
    __tablename__ = "partners"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    name = Column(String(80), nullable=False)
    axolotl_commission = Column(Integer, nullable=False)
    createAt = Column(DateTime, default=datetime.now)
    updateAt = Column(DateTime)
    deleteAt = Column(DateTime)
    active = Column(Boolean, default=True)

class Partners_repository:
    async def save(self, **partner: dict):
        try:
            new_partner = Partners(**partner)
            session.add(new_partner)
            session.commit()
            return new_partner
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}

    async def find(self, **partner: dict):
        try:
            return session.query(Partners).filter_by(**partner).all()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def find_one(self, **partner: dict):
        try:
            return session.query(Partners).filter_by(**partner).first()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def update(self, **partner: dict):
        try:
            partner["updateAt"] = datetime.now()
            update = (
                session.query(Partners)
                .filter_by(id = partner["id"])
                .update(partner, synchronize_session="fetch")
            )
            session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}