from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


class RegisterView(APIView): 
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginView(APIView): 
    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()
        print(user)

        if user is None:
            return Response({'detail':'user not found'})
        
        if not user.check_password(password):
            return Response({'detail':'Incorrect password'})
        
        return Response({
            'message':'Success!!!'
        })