from django.urls import path, include
from .views import UserApiListAPIView


app_name = 'userapp_api'

urlpatterns = [
    path('', UserApiListAPIView.as_view()),
]
