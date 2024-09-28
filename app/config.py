
# from pydantic_settings import BaseSettings
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Configuration():
    ENV = getenv("SERVER_ENV")
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
        getenv("DB_NAME"),
        getenv("DB_USER"),
        getenv("DB_PASSWORD"),
        getenv("DB_HOST"),
        getenv("DB_PORT"),
        getenv("DB_DATABASE"),
    )
    SECRET_KEY = getenv("SECRET_KEY")
    ALGORITHM = getenv("ALGORITHM")

    APP_NAME="URPSalesSystem"
    ADMIN_EMAIL="fernando.cortes@axolotlcode.com"
    SERVER_DEBUG=getenv("SERVER_DEBUG")

config = Configuration()