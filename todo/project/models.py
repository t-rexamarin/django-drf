from django.db import models
from usersapp.models import User


# Create your models here.
class ActiveProjectsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveProjectsManager, self).get_queryset().filter(is_active=True)


class ActiveTodoManager(models.Manager):
    def get_queryset(self):
        return super(ActiveTodoManager, self).get_queryset().filter(is_active=True)


class Project(models.Model):
    objects = models.Manager()
    active = ActiveProjectsManager()

    name = models.CharField(max_length=80)
    link = models.URLField()
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Todo(models.Model):
    objects = models.Manager()
    active = ActiveTodoManager()

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=300, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
