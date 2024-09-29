from . import Error

class UserException:

    def not_found():
        Error("User not found or inactive", 404)

    def user_exist():
        Error("User with this email already exists", 409)

    def not_created():
        Error("A problem occurred while creating the user", 400)

    def not_updated():
        Error("A problem occurred while updating the user", 400)

    def not_deleted():
        Error("A problem occurred while deleting the user", 400)