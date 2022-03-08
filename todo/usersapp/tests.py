import math
import os
from django.core.wsgi import get_wsgi_application

from project.models import Project, Todo

os.environ['DJANGO_SETTINGS_MODULE'] = 'todo.settings'
application = get_wsgi_application()

from dateutil.tz import tzoffset
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient,\
    APISimpleTestCase, APITestCase, CoreAPIClient
from usersapp.views import UserModelViewSet
from usersapp.models import User


# Create your tests here.
class TestUserViewSet(TestCase):
    def setUp(self):
        self.admin_name = 'django'
        self.admin_pass = '1'
        self.admin_email = 'admin@email.admin'
        self.admin = User.objects.create_superuser(self.admin_name, self.admin_email, self.admin_pass)
        self.url = '/api/users/viewsets/base/'

        self.data = {
            'username': 'test_username',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.test',
            #'birthday_date': datetime(1990, 9, 9, tzinfo=tzoffset('Europe/Moscow', 3*60*60)),
            #'password': '1'
        }

        self.data_updated = {
            'username': 'test_username_upd',
            'first_name': 'test_first_name_upd',
            'last_name': 'test_last_name_upd',
            'email': 'test@test.testupd',
            #'birthday_date': datetime(2000, 1, 1, tzinfo=tzoffset('Europe/Moscow', 3*60*60)),
            #'password': '2'
        }

    # <-- APIRequestFactory -->
    def test_get_user_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data, format='json')
        force_authenticate(request, self.admin)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    # <-- APIRequestFactory -->

    # <-- APIClient -->
    def test_get_detail(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.get(path=f'{self.url}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_guest(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        response = client.put(path=f'{self.url}{user.id}/',
                              data=self.data_updated)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_admin(self):
        client = APIClient()
        user = User.objects.create(**self.data)
        print(user.id)
        client.login(username=self.admin_name,
                     password=self.admin_pass)
        response = client.put(path=f'{self.url}{user.id}/',
                              data=self.data_updated)
        # дебаг, долго возился, не так был задан емейл
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user_ = User.objects.get(id=user.id)
        self.assertEqual(user_.first_name, self.data_updated.get('first_name'))
        self.assertEqual(user_.last_name, self.data_updated.get('last_name'))
        self.assertEqual(user_.birthday_date, self.data_updated.get('birthday_date'))
        client.logout()
    # <-- APIClient -->

    def tearDown(self) -> None:
        pass


# <-- APISimpleTestCase -->
class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)
# <-- APISimpleTestCase -->


# <-- APITestCase -->
class TestProject(APITestCase):
    def setUp(self):
        self.admin_name = 'django'
        self.admin_pass = '1'
        self.admin_email = 'admin@email.admin'
        self.admin = User.objects.create_superuser(self.admin_name, self.admin_email, self.admin_pass)
        self.url = '/api/projects/viewsets/project/'

        self.data = {
            'username': 'test_username',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.test',
            #'birthday_date': datetime(1990, 9, 9, tzinfo=tzoffset('Europe/Moscow', 3*60*60)),
            'password': '1'
        }

        self.data_updated = {
            'username': 'test_username_upd',
            'first_name': 'test_first_name_upd',
            'last_name': 'test_last_name_upd',
            'email': 'test@test.test_upd',
            #'birthday_date': datetime(2000, 1, 1, tzinfo=tzoffset('Europe/Moscow', 3*60*60)),
            'password': '2'
        }

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_admin(self):
        proj_name = 'test_proj'
        proj_name_new = 'test_proj_new'
        user = User.objects.create(**self.data)

        project = Project()
        project.name = proj_name
        project.link = 'test_proj_link'
        project.is_active = 1
        project.save()
        # нашел такой сопособ, из-за мени-ту-мени
        project.users.set(User.objects.filter(id=user.id))

        Todo.objects.create(
            project=project,
            text='test_text',
            owner=user,
            is_active=1
        )

        self.client.login(username=self.admin_name,
                          password=self.admin_pass)

        response = self.client.put(path=f'{self.url}{project.id}/',
                                   data={'name': proj_name_new})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project_ = Project.objects.get(id=project.id)
        self.assertEqual(project_.name, proj_name_new)
        self.client.logout()
# <-- APITestCase -->


# <-- CoreAPIClient -->
class UserLiveTest(TestCase):
    def setUp(self):
        self.admin_name = 'django'
        self.admin_pass = '1'
        self.admin_email = 'admin@email.admin'
        self.admin = User.objects.create_superuser(self.admin_name, self.admin_email, self.admin_pass)
        self.url = 'http://127.0.0.1:8000/api/users/viewsets/base/'

        self.data = {
            'username': 'test_username',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.test',
            #'birthday_date': datetime(1990, 9, 9, tzinfo=tzoffset('Europe/Moscow', 3*60*60)),
            'password': '1'
        }

    def test_live_user(self):
        client = CoreAPIClient()
        schema = client.get(self.url)
        client.action(schema, ['base', 'create'], self.data)

        data = client.action(schema, ['base', 'create'])
        assert(len(data) == 1)
# <-- CoreAPIClient -->