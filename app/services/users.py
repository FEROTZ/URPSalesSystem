from sqlalchemy.orm import Session
from ..exceptions.user_exception import UserException
from ..models.Users import User
from .roles import RoleService
from ..utils.validate_attribute import validateAttribute
from ..dto import (
    CreateUserInputSchema,
    GetAllUsersOutputSchema,
    GetUserOutputSchema,
    UserSchema,
    UpdateUserInputSchema
)

class UserService:

    def get(db: Session, user_id: int):
        get_user = User.find_one(db=db, id = user_id, status = 'active')

        if not get_user:
            UserException.not_found()

        response = GetUserOutputSchema(
            success = True,
            message = "User was obtained successfully",
            payload = UserSchema.model_validate(get_user)
        )

        return response


    def get_all(db: Session):
        get_all_users = User.find(db=db)

        if not get_all_users:
            UserException.users_not_found()

        response = GetAllUsersOutputSchema(
            success=True,
            message="Users were obtained successfully",
            payload=[UserSchema.model_validate(user) for user in get_all_users]
        )
        return response

    def create(db: Session, body: CreateUserInputSchema):
        body = body.model_dump(exclude_unset=True)
        exist = User.find_one(db=db, email=body['email'], status='active')
        if exist:
            UserException.user_exist()

        get_role = RoleService.get_none_admin_role(db = db)
        if get_role:
            body['role_id'] = get_role.id

        new_user = User.save(db = db, **body)

        if not new_user:
            UserException.not_created()
        user = User.find_one(db=db, id=new_user.id)

        response = {}
        response['success'] = True
        response['message'] = "User created successfully"
        response['payload'] = user.__dict__

        return response

    def update(db: Session, user_id: int, body: UpdateUserInputSchema):
        body = body.model_dump(exclude_unset=True)

        if not body:
            UserException.not_updated()

        user = User.find_one(db=db, id = user_id, status = 'active')
        if not user:
            UserException.not_found()

        if validateAttribute(body, 'password'):
            hashed_password = User.hash_password(body['password'])
            body['password'] = hashed_password

        update_user = User.update(db = db, user_id = user_id, **body)

        if not update_user:
            UserException.not_updated()
        user = User.find_one(db=db, id = user_id, status = 'active')
        print(user.__dict__)
        response = {}
        response['success'] = True
        response['message'] = "User updated successfully"
        response['payload'] = user.__dict__

        return response

    def deactive_user(db: Session, user_id: int):
        get_user = User.find_one(db=db, id = user_id, status = 'active')
        if not get_user:
            UserException.not_found()

        User.delete(db = db, id = user_id)

        user = User.find_one(db=db, id = user_id, status = 'inactive')
        if not user:
            UserException.not_deleted()

        response = {}
        response['success'] = True
        response['message'] = "User deleted successfully"
        response['payload'] = user.__dict__

        return response

    def change_role(db: Session, user_id: int, body: UpdateUserInputSchema):
        body = body.model_dump(exclude_unset=True)

        get_role = RoleService.get(db = db, role_id = body['role_id'])

        update_role = User.update(db = db, user_id = user_id, role_id = body['role_id'])

        if not update_role:
            UserException.not_updated()

        user = User.find_one(db=db, id = user_id, status = 'active')

        response = GetUserOutputSchema(
            success = True,
            message = "User role updated successfully",
            payload = UserSchema.model_validate(user)
        )
        return response
