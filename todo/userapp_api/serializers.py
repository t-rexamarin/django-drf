from rest_framework.serializers import ModelSerializer
from usersapp.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'birthday_date')


class UserExtendedModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'birthday_date',
                  'is_staff',
                  'is_superuser')
