from rest_framework import serializers
from users.models import *


class SubAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subadmins
        fields = ['company_name','company_address','service_type','user']

