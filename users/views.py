from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from users.models import *


class RegisterView(APIView): 
    def post(self,request):
        try:
            print(request.data,"request.dataaaaaaaaaaa")
            if request.data["password"] != request.data["conformPassword"]:
                return Response({'error':'passwords do not match'})
            serializer = UserSerializer(data=request.data)
            print(request.data,"request.dataaaaaaaaaaa")
            print(serializer,"serializerrrrrrrrrrrrrrr")
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'detail':'User created successfully','data':serializer.data})
        except Exception as e:
            return Response({'error':str(e)})
    
class LoginView(APIView): 
    def post(self,request):
        try:
            email = request.data["email"]
            password = request.data["password"]

            user = User.objects.filter(email=email).first()
            print(user)

            if user is None:
                return Response({'error':'user not found'})
            
            if not user.check_password(password):
                return Response({'error':'Incorrect password'})
            
            return Response({
                'message':'Success!!!',
                'user':user.username,
                'email':user.email,
                })
        except Exception as e:
            return Response({'error':str(e)})
    
class CreateSubAdmin(APIView):
    def post(self,request):
        try:
            serializer = SubadminsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'detail':'Subadmin created successfully','data':serializer.data})
        except Exception as e:
            return Response({'error':str(e)})

    
