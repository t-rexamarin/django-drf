from django.contrib import admin
from usersapp.models import User
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
