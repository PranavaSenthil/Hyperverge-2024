from rest_framework import serializers
from users.models import *
from users.serializers import *

class SubAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subadmins
        fields = ['company_name','company_address','service_type','user']

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ['id','name','description']

class RatingsReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ratings_reviews
        fields = ['id','company','rating','review']

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem
        fields = ['id','date','problem_discription','time','customer','company_name','tagged_worker']