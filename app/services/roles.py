from sqlalchemy.orm import Session
from ..exceptions.role_exception import RoleException
from ..models.Roles import Role
# from ..models import Role as model
# from ..schemas import Role as schema
from ..dto import CreateRoleInputSchema, GetAllRolesOutputSchema, RoleSchema, GetRoleOutputSchema
# import random

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



# def update_role(db: Session, role_id: int, role_update: schema.RoleUpdate):
#     role = get_role(db, role_id=role_id)

#     update_role = role_update.model_dump(exclude_unset=True)

#     for key, value in update_role.items():
#         setattr(role, key, value)
#     db.commit()
#     db.refresh(role)
#     return role


# def delete_role(db: Session, role_id: int):
#     role = get_role(db, role_id=role_id)

#     role.status = schema.RoleStatusType.inactive
#     db.commit()
#     db.refresh(role)
#     return role


# def get_none_admin_role(db: Session):
#     non_admin_roles = db.query(model).filter(model.name != 'admin').all()
#     return random.choice(non_admin_roles) if non_admin_roles else None