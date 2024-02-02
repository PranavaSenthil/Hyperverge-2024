from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from FetchAPI.serializer import SubAdminSerializer
from users.models import *

# for superadmin
class SubAdmingetView(APIView):
    def get(self,request):
        try:
            sub_admin = Subadmins.objects.all()
            serializer = SubAdminSerializer(sub_admin,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)})
