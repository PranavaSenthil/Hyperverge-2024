from django.urls import path,include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('get_SubAdmin/',SubAdmingetView.as_view()),
    path('get_ServiceType/',ServiceTypeview.as_view()),
    path('get_nearbySubadmin/',CompanyView.as_view()),
    path('assign_worker/',AssignWorker.as_view()),
]
