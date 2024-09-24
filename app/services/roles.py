from sqlalchemy.orm import Session
# from .. import models, schemas
from ..models import Role as model
from ..schemas import Role as schema
import random


def get_role(db: Session, role_id: int):
    return db.query(model).filter(model.id == role_id, model.status == 'active').first()


def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model).filter(model.status == 'active').offset(skip).limit(limit).all()


def get_role_by_name(db: Session, name: str):
    return db.query(model).filter(
        model.name == name,
    ).first()

def create_role(db: Session, role: schema.RoleCreate):
    new_role = model(
        name=role.name,
        description=role.description if role.description else None,
    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


def update_role(db: Session, role_id: int, role_update: schema.RoleUpdate):
    role = get_role(db, role_id=role_id)

    update_role = role_update.model_dump(exclude_unset=True)
    
    for key, value in update_role.items():
        setattr(role, key, value)
    db.commit()
    db.refresh(role)
    return role


def delete_role(db: Session, role_id: int):
    role = get_role(db, role_id=role_id)
    
    role.status = schema.RoleStatusType.inactive
    db.commit()
    db.refresh(role)
    return role


def get_none_admin_role(db: Session):
    non_admin_roles = db.query(model).filter(model.name != 'admin').all()
    return random.choice(non_admin_roles) if non_admin_roles else None