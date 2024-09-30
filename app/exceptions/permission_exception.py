from . import Error


class PermissionException(Error):

    def not_found():
        Error("Permission not found or inactive", 404)

    def permissions_not_found():
        Error("No permissions found", 404)

    def permission_exist():
        Error("Permission with this name already exist", 409)

    def not_created():
        Error("A problem occurred while creating the permission", 400)

    def not_updated():
        Error("A problem occurred while updating the permission", 400)

    def not_deleted():
        Error("A problem occurred while deleting the permission", 400)