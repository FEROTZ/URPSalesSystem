from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.roles import RoleService
from ..database import get_db
from ..dto import (
    CreateRoleInputSchema,
    CreateRoleOutputSchema,
    GetAllRolesOutputSchema,
    GetRoleOutputSchema,
    UpdateRoleOutputSchema,
    UpdateRoleInputSchema,
    DeleteRoleOutputSchema
)


class Role():
    router = APIRouter()

    @router.get('/', response_model = GetAllRolesOutputSchema, status_code = status.HTTP_200_OK)
    def list_roles(db: Session = Depends(get_db)):
        return RoleService.get_all(db = db)

    @router.get('/{role_id}', response_model = GetRoleOutputSchema, status_code = status.HTTP_200_OK)
    def role_details(role_id: int, db: Session = Depends(get_db)):
        return RoleService.get(db = db, role_id = role_id)

    @router.post('/create', response_model = CreateRoleOutputSchema, status_code = status.HTTP_201_CREATED)
    def create_user(body: CreateRoleInputSchema, db: Session = Depends(get_db)):
        return RoleService.create(db = db, body = body)

    @router.put('/{role_id}', response_model = UpdateRoleOutputSchema, status_code = status.HTTP_200_OK)
    def update_role(role_id: int, body: UpdateRoleInputSchema, db: Session = Depends(get_db)):
        return RoleService.update(db = db, role_id = role_id, body = body)

    @router.delete('/{role_id}', response_model = DeleteRoleOutputSchema, status_code = status.HTTP_200_OK)
    def delete_role(role_id: int, db: Session = Depends(get_db)):
        return RoleService.deactive_role(db = db, role_id = role_id)