from sqlalchemy.orm import Session
from ..exceptions.permission_exception import PermissionException
from ..models.Permissions import Permission
from ..dto import (
    CreatePermissionInputSchema,
)

class PermissionService:

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