from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, UserMinSerializer


class UsersPermissionMixin(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    def get_permissions(self):
        if self.action in ["signup", "login"]:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == "signup":
            return UserSerializer
        return UserMinSerializer
