from sqlalchemy.orm import Session
from ..exceptions.permission_exception import PermissionException
from ..models.Permissions import Permission
from ..dto import (
    CreatePermissionInputSchema,
    PermissionSchema,
    GetAllPermissionsOutputSchema,
    GetPermissionOutputSchema,
    UpdatePermissionInputSchema,
)

class PermissionService:

    def get(db: Session, permission_id: int):
        get_permission = Permission.find_one(db = db, id = permission_id, status = 'active')

        if not get_permission:
            PermissionException.not_found()

        response = GetPermissionOutputSchema(
            success = True,
            message = "Permission was obtained successfully",
            payload = PermissionSchema.model_validate(get_permission)
        )

        return response

    def get_all(db: Session):
        get_all_permissions = Permission.find(db = db)

        if not get_all_permissions:
            PermissionException.permissions_not_found()

        response = GetAllPermissionsOutputSchema(
            success = True,
            message = "Permissions were obtained successfully",
            payload = [PermissionSchema.model_validate(permission) for permission in get_all_permissions]
        )

        return response

    def create(db: Session, body: CreatePermissionInputSchema):
        body = body.model_dump(exclude_unset=True)

        exist = Permission.find_one(db = db, name = body['name'])
        if exist:
            PermissionException.permission_exist()

        new_permission = Permission.save(db = db, **body)

        if not new_permission:
            PermissionException.not_created()

        permission = Permission.find_one(db = db, id = new_permission.id)

        response = {}
        response['success'] = True
        response['message'] = "Permission created successfully"
        response['payload'] = permission.__dict__

        return response

    def update(db: Session, permission_id: int, body: UpdatePermissionInputSchema):
        body = body.model_dump(exclude_unset=True)

        if not body:
            PermissionException.not_updated()

        get_permission = Permission.find_one(db = db, id = permission_id, status = 'active')

        if not get_permission:
            PermissionException.not_found()

        permission_update = Permission.update(db = db, permission_id = permission_id, **body)

        if not permission_update:
            PermissionException.not_updated()

        permission = Permission.find_one(db = db, id = permission_id, status = 'active')

        response = {}
        response['success'] = True
        response['message'] = "Permission updated successfully"
        response['payload'] = get_permission.__dict__

        return response