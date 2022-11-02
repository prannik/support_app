from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from app.account.serializers import LogInSerializer, SignUpSerializer, SignUpStaffSerializer


class AuthViewSet(GenericViewSet):
    serializer_classes = {
        'signup': SignUpSerializer,
        'login': LogInSerializer,
        'signup_staff': SignUpStaffSerializer
    }
    permission_classes = {'signup_staff': IsAdminUser}

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, Serializer)

    def get_permissions(self):
        permission_class = self.permission_classes.get(self.action, AllowAny)
        return [permission_class()]

    @action(methods=('POST',), detail=False)
    def signup(self, request):
        """  Signup  """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=('POST',), detail=False)
    def login(self, request):
        """ Login   """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=('POST',), detail=False)
    def signup_staff(self, request):
        """ Signup Admin view"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
