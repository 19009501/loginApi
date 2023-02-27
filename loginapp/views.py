from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer
# class LoginAPIView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
#         if user:
            # Login successful
        #     return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        # else:
        #     # Invalid email or password
        #     return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import CustomUser
class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    def get(self,request):
        queryset=CustomUser.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return Response(serializer.data)
