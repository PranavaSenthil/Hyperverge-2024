from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from FetchAPI.serializer import SubAdminSerializer,ServiceTypeSerializer,RatingsReviewsSerializer
from users.serializers import *
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

class ServiceTypeview(APIView):
    def get(self,request):
        try:
            service_type = ServiceType.objects.all()
            serializer = ServiceTypeSerializer(service_type,many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error':str(e)})
        
class CompanyView(APIView):
    def get(self,request,*kwargs):
        try:
            service_id = request.GET.get('service_id')
            area = request.GET.get('area')
            subarea = request.GET.get('subarea')
            company = Subadmins.objects.filter(service_type_id=service_id,company_area=area)
            if company is None:
                company = Subadmins.objects.filter(service_type_id=service_id,company_area=subarea)
            serializer = SubadminsSerializer(company,many=True)
            rating_review = []
            for field in company:
                ratings = ratings_reviews.objects.filter(company_id=field.id)
                rating_serializer = RatingsReviewsSerializer(ratings,many=True)
                rating_review.append(rating_serializer.data)

            return Response({"subadmins": serializer.data, "ratings_reviews": rating_review})
        except Exception as e:
            return Response({'error':str(e)})
        
class AssignWorker(APIView):
    def get(self,request,*kwargs):
        try:
            comp_id = request.GET.get('company_id')
            problems = problem.objects.filter(company_name_id=comp_id)
            worker = UserRecord.objects.filter(subadmin_id=comp_id)
            serializer = ProblemSerializer(problems,many=True)
            workerserializer = UserRecordSerializer(worker,many=True)
            return Response({'serializer':serializer.data,'worker':workerserializer.data})
        except Exception as e:
            return Response({'error':str(e)})
    
class ViewWorkertasks(APIView):
    def get(self,request,*kwargs):
        try:
            worker_id = request.GET.get('worker_id')
            problems = problem.objects.filter(tagged_worker_id=worker_id)
            print(problems)
            serializer = ProblemSerializer(problems,many=True)
            return Response({'serializer':serializer.data})
        except Exception as e:
            return Response({'error':str(e)})