from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from djangorestframework_camel_case.render import CamelCaseBrowsableAPIRenderer, CamelCaseJSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework import mixins
from usersapp.models import User
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
import django_filters


# Create your views here.
class ProjectSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # я не понимаю на что влияет
    # max_page_size = 3


class ProjectViewSet(GenericViewSet, mixins.CreateModelMixin):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    serializer_class = ProjectModelSerializer
    # pagination_class = ProjectSetPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()

        if name:
            projects = projects.filter(name__contains=name)

        # pagination from base settings
        # projects = self.paginate_queryset(projects)
        return projects

    # пытка сделать свой
    # уперся в непонимание того, как мультипл чоис с юзерами обработать
    # только последний попадает
    # def create(self, request, *args, **kwargs):
    #     project = Project()
    #     project.name = request.POST['name']
    #     project.link = request.POST['link']
    #     project.is_active = True if request.POST['is_active'] == 'true' else False
    #     project.save()
    #     user_pk = request.POST['users']
    #     user = [User.objects.get(id=int(user_pk))]
    #     project.users.set(user)
        # serializer = ProjectModelSerializer(project, data=request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # return Response(serializer.data)

    # http://127.0.0.1:8000/api/projects/viewsets/project/
    def list(self, request):
        projects = self.get_queryset()
        page = self.paginate_queryset(projects)

        if page:
            serializer = ProjectModelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = ProjectModelSerializer(projects, many=True)
            return Response(serializer.data)
        # serializer = ProjectModelSerializer(projects, many=True)
        # return Response(serializer.data)

    # http://127.0.0.1:8000/api/projects/viewsets/project/28/
    def retrieve(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project)
        return Response(serializer.data)

    def update(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        project = Project.objects.get(pk=self.kwargs['pk'])
        project.is_active = False
        project.save()
        response = self.serializer_class(project).data
        return Response(response)


class TodoSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'


class TodoFilter(django_filters.FilterSet):
    # created_gte = django_filters.DateFilter(field_name='created', lookup_expr='gte')
    # created_lte = django_filters.DateFilter(field_name='created', lookup_expr='lte')
    created_between = django_filters.DateFromToRangeFilter(field_name='created', label='created between')

    class Meta:
        model = Todo
        fields = ['created_between']


class TodoViewSet(GenericViewSet, mixins.CreateModelMixin):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    serializer_class = TodoModelSerializer
    # pagination_class = TodoSetPagination
    # filter_backends = (DjangoFilterBackend,)
    filterset_class = TodoFilter

    def get_queryset(self):
        project_name = self.request.query_params.get('project_name', '')
        created_between_after = self.request.query_params.get('created_between_after', '')
        created_between_before = self.request.query_params.get('created_between_before', '')
        todos = Todo.objects.all()

        if created_between_after:
            todos = todos.filter(created__gte=created_between_after)

        if created_between_before:
            todos = todos.filter(created__lte=created_between_before)

        if project_name:
            todos = todos.filter(project__name__contains=project_name)
        return todos

    # http://127.0.0.1:8000/api/projects/viewsets/todo/
    def list(self, request):
        todos = self.get_queryset()
        page = self.paginate_queryset(todos)

        if page:
            serializer = TodoModelSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = TodoModelSerializer(todos, many=True)
            return Response(serializer.data)

    # http://127.0.0.1:8000/api/projects/viewsets/todo/196/
    def retrieve(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def update(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs['pk'])
        todo.is_active = False
        todo.save()
        response = self.serializer_class(todo).data
        return Response(response)


# class ProjectModelViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer


# class TodoModelViewSet(ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoModelSerializer
#
#     def destroy(self, request, *args, **kwargs):
#         todo = Todo.objects.get(pk=self.kwargs['pk'])
#         todo.is_active = False
#         todo.save()
#         response = self.serializer_class(todo).data
#         return Response(response)
