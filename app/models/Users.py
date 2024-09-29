from sqlalchemy import Column, Integer, String, Enum, DateTime, ForeignKey, exc
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from ..database import Base, get_db
from passlib.context import CryptContext

db: Session = get_db()

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

    # def __repr__(self):
    #     return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

    def save(**kwargs):
        try:
            user = User(**kwargs)
            password = User.hash_password(user['password'])
            user['password'] = password
            db.session.add(user)
            db.session.commit()
            db.refresh(user)
            return user
        except Exception as error:
            print(error)
            return {}
        finally:
            pass


    def find(limit:int = 10, skip:int = 0):
        try:
            return db.query(User).filter_by(User.status == 'active').offset(skip).limit(limit).all()
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.query(User).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as error:
            print(error)
            return {}
        finally:
            pass

    def update(**update):
        try:
            user = (
                db.query(User).filter_by(id=str(update["id"]))
                .update(update, synchronize_session="fetch")
            )
            db.commit()
            db.refresh(user)
            return user
        except Exception as error:
            print(error)
            db.rollback()
            return {}

    def delete(**kwargs):
        try:
            user = (
                db.query(User).filter_by(**kwargs)
                .update({
                    "status": "inactive",
                    "deleted_at": datetime.now(),
                },synchronize_session="fetch")
            )
            db.commit()
            db.refresh(user)
            return user
        except exc.SQLAlchemyError as error:
            print(error)
            db.rollback()
            return {}

    def hash_password(password: str) -> str:
        return pswd_context.hash(password)

    def verify_password(password: str, hashed_password: str) -> bool:
        return pswd_context.verify(password, hashed_password)