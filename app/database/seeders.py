from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.Roles import Role
from app.models.Permissions import Permission
from app.models.Role_Permissions import roles_permissions  # Asumiendo que este es el nombre de la tabla

def seed_roles_and_permissions(db: Session):
    try:
        # Roles
        roles = [
            {"name": "Administrator", "description": "Tiene acceso a todas las funcionalidades del sistema."},
            {"name": "Manager", "description": "Puede gestionar usuarios."},
            {"name": "Seller", "description": "Puede consultar todas las ventas del sistema."}
        ]

        # Permisos
        permissions = [
            {"name": "create_users", "description": "Permite crear nuevos usuarios"},
            {"name": "update_users", "description": "Permite actualizar usuarios existentes"},
            {"name": "delete_users", "description": "Permite eliminar usuarios"},
            {"name": "get_users", "description": "Permite consultar información de usuarios"},
            {"name": "create_roles", "description": "Permite crear nuevos roles"},
            {"name": "update_roles", "description": "Permite actualizar roles existentes"},
            {"name": "delete_roles", "description": "Permite eliminar roles"},
            {"name": "get_roles", "description": "Permite consultar información de roles"},
            {"name": "create_permissions", "description": "Permite crear nuevos permisos"},
            {"name": "update_permissions", "description": "Permite actualizar permisos existentes"},
            {"name": "delete_permissions", "description": "Permite eliminar permisos"},
            {"name": "get_permissions", "description": "Permite consultar información de permisos"},
            {"name": "get_sales", "description": "Permite consultar todas las ventas"},
            {"name": "manage_users", "description": "Permite a los vendedores gestionar usuarios"}
        ]

        # Crear roles
        db_roles = {}
        for role in roles:
            db_role = Role(**role)
            db.add(db_role)
        db.flush()

        for db_role in db.query(Role).all():
            db_roles[db_role.name] = db_role

        # Crear permisos
        db_permissions = {}
        for permission in permissions:
            db_permission = Permission(**permission)
            db.add(db_permission)
        db.flush()

        for db_permission in db.query(Permission).all():
            db_permissions[db_permission.name] = db_permission

        # Asignar permisos a roles
        role_permissions = {
            "Administrator": [p["name"] for p in permissions],
            "Manager": ["create_users", "update_users", "delete_users", "get_users"],
            "Seller": ["get_sales"]
        }

        for role_name, permissions in role_permissions.items():
            role = db_roles[role_name]
            for permission_name in permissions:
                permission = db_permissions[permission_name]
                role.permissions.append(permission)  # Asumiendo que tienes una relación many-to-many definida en tus modelos

        db.commit()
        print("Roles y permisos creados exitosamente.")

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear roles y permisos: {str(e)}")
        raise

# Función para ejecutar el seeder
def run_seeders(db: Session):
    try:
        seed_roles_and_permissions(db)
        print("Seeders ejecutados exitosamente.")
    except Exception as e:
        print(f"Error al ejecutar los seeders: {str(e)}")