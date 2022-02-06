from django.core.management.base import BaseCommand
from usersapp.models import User
from faker import Faker
import traceback
import pytz
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        # quantity of test objects
        USER_QUANTITY = 10
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
        except Exception as _:
            traceback.print_exc()
