from django.urls import path, include
from usersapp.views import UserRetrieveAPIView, UserListAPIView, UserUpdateAPIView, UserViewSet
from rest_framework.routers import DefaultRouter


app_name = 'user'

router = DefaultRouter()
router.register('base', UserViewSet, basename='user')

# TODO:
# - list
# - one
# - update
urlpatterns = [
    path('viewsets/', include(router.urls)),
    # path('generic/list/', UserListAPIView.as_view()),
    # path('generic/retrieve/<int:pk>/', UserRetrieveAPIView.as_view()),
    # path('generic/update/<int:pk>/', UserUpdateAPIView.as_view()),
]
