from django.urls import path
from usersapp.views import UserRetrieveAPIView, UserListAPIView, UserUpdateAPIView


app_name = 'user'

# TODO:
# - list
# - one
# - update
urlpatterns = [
    path('generic/list/', UserListAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('generic/update/<int:pk>/', UserUpdateAPIView.as_view()),
]
