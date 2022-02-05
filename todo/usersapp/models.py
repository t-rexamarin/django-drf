from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class ActiveUsersManager(models.Manager):
    def get_queryset(self):
        return super(ActiveUsersManager, self).get_queryset().filter(is_active=True)


class User(AbstractUser):
    objects = UserManager()
    active = ActiveUsersManager()

    email = models.EmailField(verbose_name='email', unique=True, null=False)
    birthday_date = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
