
from django.urls import path,include
from django.conf.urls.static import static
from .views import RegisterView,LoginView,CreateSubAdmin

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('create_subadmin/',CreateSubAdmin.as_view()),
    # path('view_subadmin/',SubadminsSerializer.as_view()),
]
