# from fastapi import FastAPI
# from pydantic_settings import BaseSettings
# from os import getenv
# import logging, coloredlogs
# # from fastapi.security import OAuth2PasswordBearer
# # from app.middleware.auth_middleware import auth_middleware
# from app.api.v1.endpoints import users, roles, permissions

# app = FastAPI()


# class Settings(BaseSettings):
#     ENV = getenv()
#     SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}/{}".format(
#         getenv("DB_NAME", default="your_db_name")
#         getenv("DB_USER", default="your_user"),
#         getenv("DB_PASSWORD", default="your_password"),
#         getenv("DB_HOST", default="your_host"),
#         getenv("DB_PORT", default="5432"),
#         getenv("DB_DATABASE", default="postgresql"),
#     )

#     SECRET_KEY: str
#     ALGORITHM: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int

#     DB_USER: str
#     DB_PASSWORD: str
#     DB_HOST: str
#     DB_NAME: str

#     @property
#     def DATABASE_URL(self):
#         return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"

#     class Config:
#         env_file = os.path.join(BASE_DIR, ".env")


# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")

# # app.middleware("http")(auth_middleware)


# app.swagger_ui_init_oauth = {
#     "usePkceWithAuthorizationCodeGrant": True,
#     "useBasicAuthenticationWithAccessCodeGrant": True
# }


# app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
# app.include_router(roles.router, prefix="/api/v1/roles", tags=["Roles"])
# app.include_router(permissions.router, prefix="/api/v1/permissions", tags=["Permissions"])

# # def create_app():
# #     app = FastAPI()
# #     app.debug = True

# #     logging.basicConfig(format="%(asctime)s %(message)s")
# #     coloredlogs.install(level="WARNING", logger=logging.getLogger(), isatty=True)
# #     coloredlogs.install(level="INFO", logger=logging.getLogger(), isatty=True)

# #     app.config()
# #     return True