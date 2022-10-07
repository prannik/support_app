from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from app.account.serializer import LogInSerializer, SignUpSerializer


class AuthViewSet(GenericViewSet):
    permission_classes = (AllowAny, )
    serializer_classes = {
        'signup': SignUpSerializer,
        'login': LogInSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, Serializer)

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
