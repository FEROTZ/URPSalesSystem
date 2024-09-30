from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.permissions import PermissionService
from ..database import get_db
from ..dto import (
    CreatePermissionInputSchema,
    CreatePermissionOutputSchema
)



class Permission:
    router = APIRouter()

    @router.post('/create', response_model=CreatePermissionOutputSchema, status_code=status.HTTP_201_CREATED)
    def create_permission(body: CreatePermissionInputSchema, db: Session = Depends(get_db)):
        return PermissionService.create(db = db, body = body)