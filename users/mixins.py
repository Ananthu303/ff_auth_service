from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated


class UsersPermissionMixin(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    def get_permissions(self):
        if self.action in ["signup", "login"]:
            return [AllowAny()]
        return [IsAuthenticated()]
