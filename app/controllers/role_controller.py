from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.roles import RoleService
from ..database import get_db
from ..dto import RoleSchema, CreateRoleInputSchema, CreateRoleOutputSchema, GetAllRolesOutputSchema


class Role():
    router = APIRouter()

    @router.get('/', response_model = GetAllRolesOutputSchema)
    def list_roles(db: Session = Depends(get_db)):
        return RoleService.get_all(db = db)

    @router.post('/create', response_model = CreateRoleOutputSchema, status_code = status.HTTP_201_CREATED)
    def create_user(body: CreateRoleInputSchema, db: Session = Depends(get_db)):
        return RoleService.create(db = db, body = body)