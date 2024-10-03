from fastapi import APIRouter

from ..dto import MainSchema
from ..utils.documentation import Documentation

main = APIRouter(tags=["main"])

mainDocumentation = Documentation.create(success=MainSchema)


@main.get(
    "/",
    description="Server Information",
    responses=mainDocumentation
)
async def sign_in():
    return {"code": 200, "message": "Server Running ...", "version": "1.0.0"}