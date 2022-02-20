from django.shortcuts import get_object_or_404
from djangorestframework_camel_case.render import CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


# Create your views here.
# ViewSet
# сделать через миксины?
class UserViewSet(viewsets.ViewSet):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]

    def get_queryset(self):
        users = User.objects.all()
        return users

    # http://127.0.0.1:8000/api/users/viewsets/base/
    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    # http://127.0.0.1:8000/api/users/viewsets/base/196/
    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# закреплял материал
# http://127.0.0.1:8000/api/users/generic/list/
# get list
class UserListAPIView(ListAPIView):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# http://127.0.0.1:8000/api/users/generic/retrieve/197/
# get one
class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


# http://127.0.0.1:8000/api/users/generic/update/196/
# get one
class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserAPIView(APIView):
    renderer_classes = [CamelCaseJSONRenderer]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)


# TODO:
# возвращает 404, почему?
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def user_view(request):
    users = User.objects.all()
    serializer = UserModelSerializer(users, many=True)
    return Response(serializer.data)
