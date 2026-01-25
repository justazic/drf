from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterSerializer, UsersListSerializer
from rest_framework import generics
from .models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
            })

        return Response({
            "msg": "Username yoki parol xato kiritildi"
        })
        
        
class UsersListAPIView(generics.ListAPIView):
    serializer_class = UsersListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]    