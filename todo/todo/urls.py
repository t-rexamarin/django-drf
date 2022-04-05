"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from userapp_api.views import UserApiListAPIView
from usersapp.views import UserModelViewSet
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from project.views import ProjectModelViewSet, TodoModelViewSet


schema_view = get_schema_view(
    openapi.Info(
        title='Todo',
        default_version='v2',
        description='Todo project',
        contact=openapi.Contact(email='test@test.ts'),
        license=openapi.License(name='MyLicense')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


router = DefaultRouter()
router.register('users', UserModelViewSet)
# router.register('projects', ProjectModelViewSet)
# router.register('todos', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-jwt-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-jwt-token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/', include(router.urls)),

    path('api/users/', include('usersapp.urls', namespace='user')),
    path('api/projects/', include('project.urls', namespace='project')),

    # path('userapp_api/<str:version>/', UserApiListAPIView.as_view())
    path('userapp-api/v1/', include('userapp_api.urls', namespace='v1')),
    path('userapp-api/v2/', include('userapp_api.urls', namespace='v2')),

    # с интерфейсом
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    # без
    path('swagger<str:format>', schema_view.without_ui()),

    path('graphql/', GraphQLView.as_view(graphiql=True)),

    path('', TemplateView.as_view(template_name='index.html'))
]

urlpatterns += staticfiles_urlpatterns()
