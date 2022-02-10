from django.test import TestCase
from .models import User
import random
from project.models import Project


# Create your tests here.
# class QueryTest(TestCase):
    # users = list(User.objects.all())
    # random_users = random.sample(list(User.objects.all()), 3)

    # print(random_u)

    # project = random.sample(list(Project.objects.all()), 1)
    # rand_proj_user = random.sample(list(project[0].users.all()), 1)
    # print(project)
    # print(rand_proj_user)

    # project = Project()
    # project.name = 'test_proj2'
    # project.link = 'http://127.0.0.1:8000/api/projects/'
    # project.is_active = 1
    # project.users.set(random_u)
    # project.save()
    #
    # # Project.objects.create(
    # #     name='test_proj',
    # #     link='http://127.0.0.1:8000/api/projects/',
    # #     is_active=1
    # # )
