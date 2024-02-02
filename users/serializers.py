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
        fields = ['id','company_name','company_description','user','company_address','company_city','company_state','company_area','company_image','service_type','working_hrs','holidays']

class UserRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecord
        fields = ['id','name','phoneNo','username','image','address','city','state','area','user_type']

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem
        fields = ['id','date','problem_discription','time','customer','company_name']