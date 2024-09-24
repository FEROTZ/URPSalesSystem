# from sqlalchemy.orm import Session
# from models import Permission
# from sqlalchemy import insert

# def seed_permissions(db:Session):
#     Session.execute(
#         insert(Permission).returning(Permission.id),
#         [
#             #Users
#             {"create_user", "permite crear un nuevo usuario"},
#             {"update_user", "permite actualizar un usuario existente"},
#             {"delete_user", "permite eliminar un usuario existente"},
#             {"list_users", "permite listar todos los usuarios"},
            
#             #Roles
#             {"create_role", "permite crear un nuevo rol"},
#             {"update_role", "permite actualizar un rol existente"},
#             {"delete_role", "permite eliminar un rol existente"},
#             {"list_roles", "permite listar todos los roles"},
            
#             #Permissions
#             {"create_permission", "permite crear un nuevo permiso"},
#             {"update_permission", "permite actualizar un permiso existente"},
#             {"delete_permission", "permite eliminar un permiso existente"},
#             {"list_permissions", "permite listar todos los permiso"}, 
            
#             #Sales
#             {"list_sales", "permite listar todas las ventas"},
            
#             #Special Permissions
#             {"manage_users", "permite a un vendedor gestionar usuarios"},
#         ]
#     )
    
# def run_seeder_permissions(db: Session):
#     exist_permissions = db.query(Permission).count()
#     if not exist_permissions:
#         seed_permissions(db)
#         print("Permissions seeded successfully.")
#     else:
#         print("Permissions already seeded.")