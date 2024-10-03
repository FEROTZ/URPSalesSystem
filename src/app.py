import logging
from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv
from .db import engine
from .controller import main
import src.models as models
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()


def app() -> FastAPI:
    try:
        models.db.metadata.create_all(bind=engine)
        logging.info("The models were created correctly")
    except Exception as e:
        print(e)
        logging.info("Models all realy exists")

    app = FastAPI(
        docs_url="/api",
        redoc_url=None,
        title="Microservice Calculadora Api",
        description="Microservice to calculadora",
        version=getenv("VERSION"),
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(main)

    return app


create_app = app()