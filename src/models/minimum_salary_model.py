from sqlalchemy import Column, String, Numeric, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import exc

from uuid import uuid4
from ..db import db, session
from datetime import datetime

class MinimumSalary(db):
    __tablename__ = "minimum_salary"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    country = Column(String(80), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    createAt = Column(DateTime, default=datetime.now)
    updateAt = Column(DateTime)
    deleteAt = Column(DateTime)
    active = Column(Boolean, default=True)

class MinimumSalary_repository:
    async def save(self, **minimum_salary: dict):
        try:
            new_minimum_salary = MinimumSalary(**minimum_salary)
            session.add(new_minimum_salary)
            session.commit()
            return new_minimum_salary
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}

    async def find(self, **minimum_salary: dict):
        try:
            return session.query(MinimumSalary).filter_by(**minimum_salary).all()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def find_one(self, **minimum_salary: dict):
        try:
            return session.query(MinimumSalary).filter_by(**minimum_salary).first()
        except exc.SQLAlchemyError as err:
            print(str(err))
            return {}

    async def update(self, **minimum_salary: dict):
        try:
            minimum_salary["updateAt"] = datetime.now()
            update = (
                session.query(MinimumSalary)
                .filter_by(id = minimum_salary["id"])
                .update(minimum_salary, synchronize_session="fetch")
            )
            session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print(str(err))
            session.rollback()
            return {}