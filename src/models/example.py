from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc
from sqlalchemy.orm import relationship

from uuid import uuid4
from ..db import db, session

class Leads(db):
    __tablename__ = "leads"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    firstName = Column(String(80), nullable=False)
    lastName = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    tpid = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    country = Column(String(80), nullable=False)
    countryPhoneCode = Column(String(80), nullable=False)
    phone = Column(String(80), nullable=False)
    startAt = Column(DateTime, default=datetime.now)
    updateAt = Column(DateTime)
    deleteAt = Column(DateTime)
    active = Column(Boolean, default=True)

class Leads_repository:
    async def save(self, lead: dict):
        try:
            new_lead = Leads(**lead)
            session.add(new_lead)
            session.commit()
            return new_lead
        except Exception as err:
            print(str(err))
            session.rollback()
            return {}
        finally:
            pass

    async def find_one(self, **lead: dict):
        try:
            return session.query(Leads).filter_by(**lead).first()
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}
        finally:
            pass

    async def update(self, **update: dict):
        try:
            update["updateAt"] = datetime.now()
            update = (
                session.query(Leads)
                .filter_by(id=update["id"])
                .update(update, synchronize_session="fetch")
            )
            session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}
        finally:
            pass