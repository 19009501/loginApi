from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import status

from .models import User
from .serializers import UserSerializer

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response(
                data={
                    "message": "Login successful."
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={
                    "message": "Login failed."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

class RegisterUsersViewSet(viewsets.ModelViewSet):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


