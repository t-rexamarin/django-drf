from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TodoViewSet
# from .views import ProjectModelViewSet

app_name = 'project'

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('todo', TodoViewSet, basename='todo')

# TODO:
# - all
urlpatterns = [
    path('viewsets/', include(router.urls)),
    # path('list/', ProjectModelViewSet.list),
    # path('retrieve/<int:pk>/', ProjectModelViewSet.retrieve),
    # path('update/<int:pk>/', ProjectModelViewSet.update),
]
