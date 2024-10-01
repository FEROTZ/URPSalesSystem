from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.permissions import PermissionService
from ..database import get_db
from ..dto import (
    CreatePermissionInputSchema,
    CreatePermissionOutputSchema,
    GetAllPermissionsOutputSchema,
    GetPermissionOutputSchema
)



class Permission:
    router = APIRouter()

    @router.get('/', response_model=GetAllPermissionsOutputSchema, status_code=status.HTTP_200_OK)
    def list_permissions(db: Session = Depends(get_db)):
        return PermissionService.get_all(db = db)

    @router.get('/{permission_id}', response_model = GetPermissionOutputSchema, status_code=status.HTTP_200_OK)
    def permission_details(permission_id: int, db: Session = Depends(get_db)):
        return PermissionService.get(db = db, permission_id = permission_id)

    @router.post('/create', response_model=CreatePermissionOutputSchema, status_code=status.HTTP_201_CREATED)
    def create_permission(body: CreatePermissionInputSchema, db: Session = Depends(get_db)):
        return PermissionService.create(db = db, body = body)