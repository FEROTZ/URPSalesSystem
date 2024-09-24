from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models, schemas
from passlib.context import CryptContext
from .roles import get_none_admin_role
import re


pswd_context = CryptContext(
    schemes=['bcrypt'],
    default='bcrypt',
    bcrypt__rounds=12,
)

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id, models.User.status == 'active').first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).filter(models.User.status == 'active').offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    random_role = get_none_admin_role(db)

    new_user = models.User(
        username    = user.username, 
        email       = user.email,
        password    = hashed_password,
        role_id     = random_role.id,
    )
        
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    user = get_user(db, user_id=user_id)
    if not user:
        return None
    update_user = user_update.model_dump(exclude_unset=True)
    
    if 'password' in update_user:
        update_user['password'] = hash_password(update_user['password'])
        
    for key, value in update_user.items():
        setattr(user, key, value)
        
    db.commit()
    db.refresh(user)
    return user

def deactive_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    
    if user.status == schemas.UserStatusType.inactive:
        return user

    user.status = schemas.UserStatusType.inactive
    db.commit()
    db.refresh(user)
    return user
 
def hash_password(password: str) -> str:
    return pswd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pswd_context.verify(plain_password, hashed_password)

def validate_password(password: str) -> dict:
    errors = []
    
    if not re.search(r'[a-z]', password):
        errors.append("one lowercase letter")
    if not re.search(r'[A-Z]', password):
        errors.append("one uppercase letter")
    if not re.search(r'\d', password):
        errors.append("one number")
        
    if errors:
        error_message = f"Password should contain at least {', '.join(errors)}"
        return {"message": error_message, "valid": False}
    
    return {"valid": True}