from sqlalchemy.orm import Session
from ..exceptions.role_exception import RoleException
from ..models.Roles import Role
from ..dto import (
    CreateRoleInputSchema,
    GetAllRolesOutputSchema,
    RoleSchema,
    GetRoleOutputSchema,
    UpdateRoleInputSchema
)

class RoleService:

    def get(db: Session, role_id: int):
        get_role = Role.find_one(db = db, id = role_id, status = 'active')

        if not get_role:
            RoleException.not_found()

        response = GetRoleOutputSchema(
            success = True,
            message = "Role was obtained successfully",
            payload = RoleSchema.model_validate(get_role)
        )

        return response


    def get_all(db: Session):
        get_all_roles = Role.find(db = db)

        if not get_all_roles:
            RoleException.roles_not_found()

        response = GetAllRolesOutputSchema(
            success = True,
            message = "Users were obtained successfully",
            payload = [RoleSchema.model_validate(role) for role in get_all_roles]
        )

        return response


    def create(db: Session, body: CreateRoleInputSchema):
        body = body.model_dump(exclude_unset=True)
        exist = Role.find_one(db = db, name = body['name'])
        if exist:
            RoleException.role_exist()

        new_role = Role.save(db = db, **body)

        if not new_role:
            RoleException.not_created()

        role = Role.find_one(db = db, id = new_role.id)

        response = {}
        response['success'] = True
        response['message'] = "Role created successfully"
        response['payload'] = role.__dict__

        return response



    def update(db: Session, role_id: int, body: UpdateRoleInputSchema):
        body = body.model_dump(exclude_unset=True)

        if not body:
            RoleException.not_updated()

        get_role = Role.find_one(db = db, id = role_id, status = 'active'  )

        if not get_role:
            RoleException.not_found()

        role_update = Role.update(db = db, role_id = role_id, **body)

        if not role_update:
            RoleException.not_updated()
        role = Role.find_one(db = db, id = role_id, status = 'active')

        response = {}
        response['success'] = True
        response['message'] = "Role updated successfully"
        response['payload'] = role.__dict__

        return response

    def deactive_role(db: Session, role_id: int):
        get_role = Role.find_one(db = db, id = role_id, status = 'active')

        if not get_role:
            RoleException.not_found()

        Role.delete(db = db, id = role_id)

        role = Role.find_one(db = db, id = role_id, status = 'inactive')

        if not role:
            RoleException.not_deleted()

        response = {}
        response['success'] = True
        response['message'] = "Role deleted successfully"
        response['payload'] = role.__dict__

        return response

    def get_none_admin_role(db: Session):
        return Role.get_random_non_admin_role(db = db)