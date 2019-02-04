from django.shortcuts import render
from .models import User
from .serializers import UserSerilizer, UserLoginSerilizer, UserLoginSerilizer123
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .serializers import LoginViewSerilizer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
#login api based with token generate
class LoginView(APIView):
    def post(self,request):
        serializer=LoginViewSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)

class LogoutView(APIView):
    authenticate_classes= (TokenAuthentication,)
    def post(self, request):
        django_logout(request)
        return Response(status=204)



@api_view(['POST'])
def user_post(request):
    user=UserSerilizer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

#user log in restapi
@api_view(['POST'])
def user_login(request):
    login=UserLoginSerilizer(data=request.data)
    if login.is_valid():
        login.save()
        return Response(login.data, status=status.HTTP_201_CREATED)
    return Response(login.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.contrib.auth import authenticate
# class LoginView(APIView):
#     permission_classes = ()
#     def post(self, request,):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({"token": user.auth_token.key})
#         else:
#             return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


# @csrf_except
# @api_view
# @permission_classes((AllowAny))
#
# def login(request):
#     user=UserLoginSerilizer(data=request.data)
#     if user.is_valid():
#         user.save()
#         user=authenticate(m)


class UserloginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class=UserLoginSerilizer123
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=UserLoginSerilizer123(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

