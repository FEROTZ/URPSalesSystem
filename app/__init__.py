from fastapi import FastAPI
from .config import config
import coloredlogs, logging
from .database import Base, engine
from .models import *


def create_app():
    app = FastAPI()
    app.debug = config.SERVER_DEBUG

    # logs configuration
    logging.basicConfig(format="%(asctime)s %(message)s")
    coloredlogs.install(level="WARNING", logger=logging.getLogger(), isatty=True)
    coloredlogs.install(level="INFO", logger=logging.getLogger(), isatty=True)

    # try create all models
    models.Base.metadata.create_all(bind=engine)
    # db = SessionLocal()  # We will create a database session using a SessionLocal class.
    # app.db = db  # Add the database session to our FastAPI application
    # db.init_app(app)

    from .controllers import (
        User,
        # Role,
        # Permission,
        # RolePermission,
    )

    app.include_router(User.router, prefix="/api/v1/users", tags=["Users"])
    # app.include_router(Role.router, prefix="/api/v1/roles", tags=["Roles"])
    # app.include_router(Permission.router, prefix="/api/v1/permissions", tags=["Permissions"])


    # db.create_all()  # Create database tables for our data models
    return app
