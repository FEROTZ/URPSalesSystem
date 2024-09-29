from sqlalchemy.orm import Session
from ..exceptions.user_exception import UserException
from .. import schemas
from ..models.Users import User
# from .roles import get_none_admin_role
import re

class UserService:

    def get(user_id: int):
        get_user = User.find_one(id=user_id, status='active')

        if not get_user:
            UserException.not_found()

        response = {}
        response['success'] = True
        response['message'] = "User fetched successfully"
        response['payload'] = get_user.__dict__

        return response


    def get_all(skip: int = 0, limit: int = 10):
        get_all_users = User.find(limit=limit, skip=skip)

        users = []
        for user in get_all_users:
            users.append(user.__dict__)

        response = {}
        response['success'] = True
        response['message'] = "Users was obtained successfully"
        response['payload'] = users

        return response

    def create(body: schemas.UserCreate):
        exist = User.find_one(email=body['email'], status='active')
        if exist:
            UserException.user_exist()

        new_user = User.save(**body)

        if not new_user:
            UserException.not_created()

        user = User.find_one(id=new_user.id)

        response = {}
        response['success'] = True
        response['message'] = "User created successfully"
        response['payload'] = user.__dict__

        return response

    # def update(body: schemas.UserUpdate):
    #     get_user = User.find_one(id = body['id'])
    #     if not get_user:
    #         UserException.not_found()

    #     if validateAttribute(body, 'active'):
    #         body['deleted_at'] = None
    #         if not body['active']:
    #             body['deleted_at'] = datetime.now()

    #     update_user = User.update(**body)
    #     update_user = user_update.model_dump(exclude_unset=True)

    #     if 'password' in update_user:
    #         update_user['password'] = hash_password(update_user['password'])

    #     for key, value in update_user.items():
    #         setattr(user, key, value)

    #     db.commit()
    #     db.refresh(user)
    #     return user

    # def deactive_user(db: Session, user_id: int):
    #     user = db.query(models.User).filter(models.User.id == user_id).first()
    #     if not user:
    #         return None

    #     if user.status == schemas.UserStatusType.inactive:
    #         return user

    #     user.status = schemas.UserStatusType.inactive
    #     db.commit()
    #     db.refresh(user)
    #     return user