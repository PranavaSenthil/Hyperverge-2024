from django.urls import path,include
from django.conf.urls.static import static
from .views import SubAdmingetView

urlpatterns = [
    path('get_SubAdmin/',SubAdmingetView.as_view()),
    
]
