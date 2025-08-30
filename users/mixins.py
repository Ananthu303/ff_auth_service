from rest_framework.permissions import AllowAny, IsAuthenticated

class UsersPermissionMixin:
    def get_permissions(self):
        if self.action in ["signup", "login"]:
            return [AllowAny()]
        return [IsAuthenticated()]
