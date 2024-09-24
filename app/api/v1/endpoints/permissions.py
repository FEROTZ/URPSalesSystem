from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.services import permissions as permissions_crud
from app.schemas import PermissionResponse, PermissionCreate, PermissionUpdate, PermissionInactiveResponse, PermissionBase
from app.database.database import get_db
from typing import List

router = APIRouter()

@router.get('/', response_model=List[PermissionBase])
async def list_permissions(
    skip: int = Query(0, ge=0, description="Number of permissions to skip."),
    limit: int = Query(10, gt=0, le=20, description="Number of permissions to return"),
    db: Session = Depends(get_db)
):
    permissions = permissions_crud.get_permissions(db, skip=skip, limit=limit)
    
    if not permissions:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail="No permissions found."
        )
        
    return permissions


@router.post('/', response_model=PermissionResponse, status_code=status.HTTP_201_CREATED)
async def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    permission_exist = permissions_crud.get_permission_by_name(db, name=permission.name)

    if permission_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Permission already exists."
        )

    new_permission = permissions_crud.create_permission(db, permission=permission)
    
    return new_permission


@router.put('/{permission_id}', response_model=PermissionResponse)
async def update_permission(permission_id: int, permission_update: PermissionUpdate, db: Session = Depends(get_db)):
    permission_exits = permissions_crud.get_permission(db, permission_id=permission_id)

    if not permission_exits:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Permission not found."
        )
    
    update_permission = permissions_crud.update_permission(db, permission_id=permission_id, permission_update=permission_update)

    return update_permission


@router.delete('/{permission_id}', response_model=PermissionInactiveResponse)
async def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    permission_exits = permissions_crud.get_permission(db, permission_id=permission_id)

    if not permission_exits:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Permission not found."
        )
    
    delete_permission = permissions_crud.delete_permission(db, permission_id=permission_id)

    return delete_permission