from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            "password":{"write_only":True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class SubadminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subadmins
        fields = ['id','company_name','company_description','user','company_address','company_city','company_state','comapany_area','comapany_image','service_type','working_hrs','holidays']