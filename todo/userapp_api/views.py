from djangorestframework_camel_case.render import CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer
from rest_framework.generics import ListAPIView
from userapp_api.serializers import UserExtendedModelSerializer, UserModelSerializer
from usersapp.models import User


# Create your views here.
class UserApiListAPIView(ListAPIView):
    renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserExtendedModelSerializer
        return UserModelSerializer
