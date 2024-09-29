from fastapi import APIRouter, Depends, Query, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
# from ..core.auth import authenticate_user, create_access_token, oauth2_scheme
from ..dto import createUserInputSchema, getUserOutputSchema, UserSchema
from app.services.users import UserService
from app.schemas import UserResponse, UserCreate, Token, UserUpdate, UserInactiveResponse
from ..database import get_db
from typing import List


class User():
    router = APIRouter()

    @router.get('/', response_model=List[UserResponse])
    async def list_users(
        skip: int = Query(0, ge=0, description='Number of users to skip.'),
        limit: int = Query(10, gt=0, le=100, description='Number of users to return.'),
    ):
        users = UserService.get_all(skip=skip, limit=limit)
        if not users:
            raise HTTPException(status_code=204, detail="No users found.")
        return users

    @router.get('/{user_id}', response_model=UserResponse)
    async def user_details(user_id: int):
        return user


    @router.post('/register', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
    async def create_user(request:Request,  user: UserCreate, db: Session = Depends(get_db)):

        return UserService.create_user(db, user=user)


    @router.put('/{user_id}', response_model=UserResponse)
    async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
        if user_update.password:
            password_validation = UserService.validate_password(user_update.password)
            
            if not password_validation['valid']:
                raise HTTPException(status_code=400, detail=password_validation['message'])

        return UserService.update_user(db, user_id=user_id, user_update=user_update)
        
        if not update_user:
            raise HTTPException(status_code=404, detail="User not found.")

        return update_user


    # @router.delete('/{user_id}', response_model=UserInactiveResponse)
    # def delete_user(user_id: int, db: Session = Depends(get_db)):
        user = UserService.deactive_user(db, user_id=user_id)
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        
        return user


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