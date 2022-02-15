from django.shortcuts import get_object_or_404
from djangorestframework_camel_case.render import CamelCaseBrowsableAPIRenderer, CamelCaseJSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer


# Create your views here.
class ProjectViewSet(ViewSet):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    serializer_class = ProjectModelSerializer

    # http://127.0.0.1:8000/api/users/viewsets/base/
    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    # http://127.0.0.1:8000/api/users/viewsets/base/196/
    def retrieve(self, request, pk):
        user = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(user)
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


# class ProjectModelViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer

    def destroy(self, request, *args, **kwargs):
        todo = Todo.objects.get(pk=self.kwargs['pk'])
        todo.is_active = False
        todo.save()
        response = self.serializer_class(todo).data
        return Response(response)
