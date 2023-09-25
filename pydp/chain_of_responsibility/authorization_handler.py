class AuthorizationHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def authorize(self, user, resource):
        pass

class RoleAuthorizationHandler(AuthorizationHandler):
    def __init__(self, role):
        super().__init__()
        self.role = role

    def authorize(self, user, resource):
        if user.has_role(self.role):
            print(f"RoleAuthorizationHandler: User '{user.name}' has '{self.role}' role. Access granted.")
        elif self.next_handler is not None:
            print(f"RoleAuthorizationHandler: User '{user.name}' does not have '{self.role}' role. Passing to the next handler.")
            self.next_handler.authorize(user, resource)
        else:
            print(f"RoleAuthorizationHandler: User '{user.name}' does not have '{self.role}' role. Access denied.")

class PermissionAuthorizationHandler(AuthorizationHandler):
    def __init__(self, permission):
        super().__init__()
        self.permission = permission

    def authorize(self, user, resource):
        if user.has_permission(self.permission):
            print(f"PermissionAuthorizationHandler: User '{user.name}' has '{self.permission}' permission. Access granted.")
        elif self.next_handler is not None:
            print(f"PermissionAuthorizationHandler: User '{user.name}' does not have '{self.permission}' permission. Passing to the next handler.")
            self.next_handler.authorize(user, resource)
        else:
            print(f"PermissionAuthorizationHandler: User '{user.name}' does not have '{self.permission}' permission. Access denied.")

class User:
    def __init__(self, name):
        self.name = name
        self.roles = []
        self.permissions = []

    def has_role(self, role):
        return role in self.roles

    def has_permission(self, permission):
        return permission in self.permissions

# Create a chain of authorization handlers
role_handler = RoleAuthorizationHandler("Admin")
permission_handler = PermissionAuthorizationHandler("Edit")

role_handler.set_next_handler(permission_handler)

# Create a user with roles and permissions
user = User("Alice")
user.roles = ["Admin", "User"]
user.permissions = ["Read"]

# Attempt to access a resource
resource = "Sensitive Document"
role_handler.authorize(user, resource)
