# from fastapi import APIRouter, Depends, Query, HTTPException, status
# from sqlalchemy.orm import Session
# from app.services import roles as roles_crud
# from app.schemas import RoleResponse, RoleCreate, RoleUpdate, RoleInactiveResponse
# from app.database.connection import get_db
# from typing import List

# router = APIRouter()

# @router.get('/', response_model=List[RoleResponse])
# async def list_roles(
#     skip: int = Query(0, ge=0, description='Number of roles to skip.'),
#     limit: int = Query(10, gt=0, le=20, description='Number of roles to return.'),
#     db: Session = Depends(get_db)
# ):
#     roles = roles_crud.get_roles(db, skip=skip, limit=limit)
#     return roles

# @router.post('/', response_model=RoleCreate)
# async def create_role(role: RoleCreate, db: Session = Depends(get_db)):
#     role_exists = roles_crud.get_role_by_name(db, name=role.name)
#     if role_exists:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="Role already exists."
#         )
#     return roles_crud.create_role(db, role=role)


# @router.put('/{role_id}', response_model=RoleResponse)
# async def update_role(role_id: int, role_update: RoleUpdate, db: Session = Depends(get_db)):
#     role = roles_crud.get_role(db, role_id=role_id)
    
#     if not role:
#         raise HTTPException(status_code=404, detail="Role not found.")

#     if not role_update:
#         raise HTTPException(status_code=400, detail="Is necessary to update at least one field.")
    
#     update_role = roles_crud.update_role(db, role_id=role_id, role_update=role_update)

#     if not update_role:
#         raise HTTPException(status_code=404, detail="Role not found.")

#     return update_role


# @router.delete('/{role_id}', response_model=RoleInactiveResponse)
# async def delete_role(role_id: int, db: Session = Depends(get_db)):
#     role_exists = roles_crud.get_role(db, role_id=role_id)
    
#     if not role_exists:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found.")

#     delete_role = roles_crud.delete_role(db, role_id=role_id)
    
#     return delete_role