from sqlalchemy.orm import Session
from ..models import Permission as model
from ..schemas import Permission as schema


def get_permission(db: Session, permission_id:int):
    return db.query(model).filter(
        model.id == permission_id,
        model.status == 'active'
    ).first()


def get_permissions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model).filter(
        model.status == 'active'
    ).offset(skip).limit(limit).all()


def create_permission(db: Session, permission: schema.PermissionCreate):
    new_permission = model(
        name = permission.name,
        description = permission.description if permission.description else None
    )
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    
    return new_permission


def update_permission(db: Session, permission_id:int, permission_update: schema.PermissionUpdate):
    permission = get_permission(db, permission_id=permission_id)
    
    request = permission_update.model_dump(exclude_unset=True)

    for key, value in request.items():
        setattr(permission, key, value)
    
    db.commit()
    db.refresh(permission)
    return permission


def delete_permission(db: Session, permission_id: int):
    permission = get_permission(db, permission_id=permission_id)
    
    permission.status = schema.PermissionStatusType.inactive
    db.commit()
    db.refresh(permission)
    return permission


def get_permission_by_name(db: Session, name: str):
    return db.query(model).filter(
        model.name == name,
    ).first()