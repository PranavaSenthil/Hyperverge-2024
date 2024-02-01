
from django.urls import path,include
from django.conf.urls.static import static
from .views import RegisterView

urlpatterns = [
    path('register/',RegisterView.as_view()),
]
