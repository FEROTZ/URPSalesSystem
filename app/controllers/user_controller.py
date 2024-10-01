from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.services.users import UserService
from ..database import get_db
from ..dto import (
    GetAllUsersOutputSchema,
    GetUserOutputSchema,
    CreateUserOutputSchema,
    CreateUserInputSchema,
    UpdateUserOutputSchema,
    UpdateUserInputSchema,
    DeleteUserOutputSchema,
    ChangeUserRoleInputSchema,
    ChangeUserRoleOutputSchema
 )


class User():
    router = APIRouter()

    @router.get('/', response_model = GetAllUsersOutputSchema)
    def list_users(db: Session = Depends(get_db)):
        return UserService.get_all(db=db)

    @router.get('/{user_id}', response_model = GetUserOutputSchema)
    def user_details(user_id: int, db: Session = Depends(get_db)):
        return UserService.get(db = db, user_id = user_id)


    @router.post('/register', response_model = CreateUserOutputSchema, status_code = status.HTTP_201_CREATED)
    def create_user(body: CreateUserInputSchema, db: Session = Depends(get_db)):
        return UserService.create(body = body, db = db)


    @router.put('/{user_id}', response_model = UpdateUserOutputSchema, status_code = status.HTTP_200_OK)
    def update_user(user_id: int, body: UpdateUserInputSchema, db: Session = Depends(get_db)):
        return UserService.update(db = db, user_id = user_id, body = body)


    @router.delete('/{user_id}', response_model = DeleteUserOutputSchema, status_code = status.HTTP_200_OK)
    def delete_user(user_id: int, db: Session = Depends(get_db)):
        return UserService.deactive_user(db = db, user_id = user_id)

    @router.put('/change-role/{user_id}', response_model = ChangeUserRoleOutputSchema, status_code = status.HTTP_200_OK)
    def change_user_role(user_id: int, body: ChangeUserRoleInputSchema, db: Session = Depends(get_db)):
        return UserService.change_role(db = db, user_id = user_id, body = body)


    # @router.post('/login', response_model=Token)
    # async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #     user = authenticate_user(db, email=form_data.username, password=form_data.password)
    #     if not user:
    #         raise HTTPException(
    #             status_code = status.HTTP_401_UNAUTHORIZED,
    #             detail = "Incorrect email or password",
    #             headers = {"WWW-Authenticate": "Bearer"},
    #         )

    #     access_token_expires = timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    #     access_token = create_access_token(
    #         data = {"sub": user.email}, expires_delta = access_token_expires
    #     )

    #     return {"access_token": access_token, "token_type": "bearer"}


    # @router.post('{user_id}/assign_permission', response_model=UserResponse)
    # def assign_permission(user_id: int, permission_id: int, db: Session = Depends(get_db)):
    #     pass