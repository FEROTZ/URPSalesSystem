from sqlalchemy.orm import Session
from ..exceptions.user_exception import UserException
from .. import schemas
from ..models.Users import User
# from .roles import get_none_admin_role
from ..dto import CreateUserInputSchema, GetAllUsersOutputSchema, GetUserOutputSchema, UserSchema

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
        new_user = User.save(db = db, **body)

        if not new_user:
            UserException.not_created()
        user = User.find_one(db=db, id=new_user.id)

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