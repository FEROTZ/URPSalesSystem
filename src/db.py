from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(
    getenv("DATABASE_NAME"),
    getenv("DATABASE_USER"),
    getenv("DATABASE_PASSWORD"),
    getenv("DATABASE_HOST"),
    getenv("DATABASE_PORT"),
    getenv("DATABASE_DB"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=0, max_overflow=-1, connect_args={}, echo=False, pool_pre_ping=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

db = declarative_base()