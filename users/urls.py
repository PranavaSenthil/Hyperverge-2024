
from django.urls import path,include
from django.conf.urls.static import static
from .views import RegisterView,LoginView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
]
