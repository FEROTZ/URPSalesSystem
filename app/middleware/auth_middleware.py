from fastapi import Request, HTTPException
import logging
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.core.config import settings
from app.database.database import SessionLocal
from app.services.users import get_user_by_email

security = HTTPBearer()

# Lista de rutas excluidas de la autenticación
EXCLUDED_PATHS = ["/api/v1/users/login", "/docs", "/openapi.json", "/api/v1/users/create"]

async def auth_middleware(request: Request, call_next):
    if request.url.path in EXCLUDED_PATHS:
        return await call_next(request)
    
    # credentials_exception = HTTPException(
    #     status_code=401,
    #     detail="Could not validate credentials",
    #     headers={"WWW-Authenticate": "Bearer"},
    # )

    try:
        auth_result = await security(request)
        if not isinstance(auth_result, HTTPAuthorizationCredentials):
            return JSONResponse(status_code=401, content={"detail": "Invalid authorization code."})
        token = auth_result.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return JSONResponse(status_code=401, content={"detail": "Invalid token payload."})
    except (JWTError, ValueError):
        return JSONResponse(status_code=401, content={"detail": "Could not validate credentials"})

    db = SessionLocal()

    try:
        user = get_user_by_email(db, email)
        if user is None:
            return JSONResponse(status_code=401, content={"detail": "User not found."})

        role = user.role
        permissions = {p.name for p in role.permissions}

        request.state.user = user
        request.state.role = role.name
        request.state.permissions = permissions

    except Exception as e:
        logging.error(f"Unexpected error in auth middleware: {str(e)}")
        return JSONResponse(status_code=500, content={"detail": "Internal server error"})
    finally:
        db.close()

    return await call_next(request)