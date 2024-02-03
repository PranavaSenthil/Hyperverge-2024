from django.urls import path,include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('create_subadmin/',CreateSubAdmin.as_view()),
    path('create_userrecord/',CreateUserRecord.as_view()),
    path('create_problem/',UserProblem.as_view()), 
    path('assign_problem/',AssignProblem.as_view()),
    path('update_status/',StatusUpdate.as_view()),

    # path('view_subadmin/',SubadminsSerializer.as_view()),
]
