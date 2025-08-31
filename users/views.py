from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.tokens import RefreshToken
from .mixins import UsersPermissionMixin
from .models import User
from .serializers import UserSerializer, LoginSerializer


class UserViewSet(UsersPermissionMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(tags=["v1"])
    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @extend_schema(tags=["v1"], request=LoginSerializer)
    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})

    @extend_schema(tags=["v1"])
    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
