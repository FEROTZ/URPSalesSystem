from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.middleware.auth_middleware import auth_middleware
from app.api.v1.endpoints import users, roles, permissions

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")

# app.middleware("http")(auth_middleware)


app.swagger_ui_init_oauth = {
    "usePkceWithAuthorizationCodeGrant": True,
    "useBasicAuthenticationWithAccessCodeGrant": True
}


app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(roles.router, prefix="/api/v1/roles", tags=["Roles"])
app.include_router(permissions.router, prefix="/api/v1/permissions", tags=["Permissions"])