from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.roles import RoleService
from ..database import get_db
from ..dto import RoleSchema, CreateRoleInputSchema, CreateRoleOutputSchema


class Role():
    router = APIRouter()

    @router.post('/create', response_model = CreateRoleOutputSchema, status_code = status.HTTP_201_CREATED)
    def create_user(body: CreateRoleInputSchema, db: Session = Depends(get_db)):
        return RoleService.create(db = db, body = body)