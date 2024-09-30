from . import Error

class RoleException:

    def not_found():
        Error("Role not found or inactive", 404)

    def roles_not_found():
        Error("No roles found", 404)

    def role_exist():
        Error("Role with this name already exist", 409)

    def not_created():
        Error("A problem ocurred while creating the role", 400)

    def not_updated():
        Error("A problem ocurred while updating the role", 400)

    def not_deleted():
        Error("A problem ocurred while deleting the role", 400)