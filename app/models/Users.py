from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, exc
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from ..database import Base
from passlib.context import CryptContext


pswd_context = CryptContext(
    schemes=['bcrypt'],
    default='bcrypt',
    bcrypt__rounds=12,
)

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
    deleted_at = Column(DateTime, nullable=True)

    role = relationship("Role", back_populates='users')
    sales = relationship("Sale", back_populates="user")

    @property
    def role_name(self):
        return self.role.name


    def save(db:Session, **kwargs):
        try:
            user = User(**kwargs)
            hashed_password = User.hash_password(kwargs['password'])
            user.password = hashed_password
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as error:
            print(error)
            return {}
        finally:
            pass


    def find(db: Session):
        try:
            return db.query(User).filter_by(status = 'active').all()
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find_one(db: Session, **kwargs):
        try:
            return db.query(User).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as error:
            print(error)
            return {}
        finally:
            pass

    def update(db: Session, user_id : int, **body):
        try:
            update_user = (
                db.query(User).
                filter_by(id = user_id, status = 'active')
                .update(body, synchronize_session="fetch")
            )
            db.commit()

            return update_user
        except Exception as error:
            print(error)
            db.rollback()
            return {}

    def delete(db: Session, **kwargs):
        try:
            delete_user = (
                db.query(User)
                .filter_by(**kwargs)
                .update({
                    "status": "inactive",
                    "deleted_at": datetime.now(),
                },synchronize_session="fetch")
            )
            db.commit()
            return delete_user
        except exc.SQLAlchemyError as error:
            print(error)
            db.rollback()
            return {}

    def hash_password(password: str) -> str:
        return pswd_context.hash(password)

    def verify_password(password: str, hashed_password: str) -> bool:
        return pswd_context.verify(password, hashed_password)