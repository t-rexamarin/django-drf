from django.core.management.base import BaseCommand
from project.models import Project, Todo
from usersapp.models import User
from faker import Faker
from random import randint, sample
import traceback
import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        # clear db
        User.objects.all().delete()
        Project.objects.all().delete()
        Todo.objects.all().delete()

        # quantity of test objects
        USER_QUANTITY = 30
        PROJECT_QUANTITY = 5
        TODOS_QUANTITY = 20
        fake = Faker()

        try:
            first_names = [fake.unique.first_name() for _ in range(USER_QUANTITY)]
            last_names = [fake.unique.last_name() for _ in range(USER_QUANTITY)]

            birthdays = [pytz.utc.localize(fake.date_time()) for _ in range(USER_QUANTITY)]
            emails = [fake.unique.email() for _ in range(USER_QUANTITY)]
            passwords = [fake.unique.password() for _ in range(USER_QUANTITY)]

            # create test users
            for fname, lname, bdate, email, password in zip(first_names, last_names, birthdays, emails, passwords):
                username = f'{fname.lower()}_{lname.lower()}'
                User.objects.create_user(
                    username=username,
                    first_name=fname,
                    last_name=lname,
                    birthday_date=bdate,
                    email=email,
                    password=password
                )

            # create superuser
            User.objects.create_superuser(
                username='django',
                email='django@django.dj',
                password='1'
            )

            # create projects
            project_name = [fake.unique.company() for _ in range(PROJECT_QUANTITY)]
            project_link = [f'http://{company.lower().replace(" ", "")}.com' for company in project_name]
            project_active = [randint(0, 1) for _ in range(PROJECT_QUANTITY)]

            for project, link, proj_active in zip(project_name, project_link, project_active):
                new_project = Project()
                new_project.name = project
                new_project.link = link
                new_project.is_active = proj_active
                new_project.save()
                project_users = sample(list(User.objects.all()), 3)
                new_project.users.set(project_users)

            # create todos
            todo_text = [fake.paragraph(nb_sentences=1, variable_nb_sentences=False) for _ in range(TODOS_QUANTITY)]
            todo_is_active = [randint(0, 1) for _ in range(TODOS_QUANTITY)]

            for text, todo_active in zip(todo_text, todo_is_active):
                get_todo_project = sample(list(Project.objects.all()), 1)
                get_toto_owner = sample(list(get_todo_project[0].users.all()), 1)
                Todo.objects.create(
                    project=get_todo_project[0],
                    text=text,
                    owner=get_toto_owner[0],
                    is_active=todo_active
                )
        except Exception as _:
            traceback.print_exc()
