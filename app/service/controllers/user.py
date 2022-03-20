from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK

from core.controllers import BaseController
from service.serializers.user import UserSerializer


class UserController(BaseController):
    """
    User Controller
    """
    serializer_class = UserSerializer
    queryset = UserSerializer.queryset

    """
    Custom API
    """

    @action(detail=True, methods=['GET'], url_path='(?P<name_pk>[^/.]+)')
    def list_name(self, request, name_pk, **kwargs):
        data = UserSerializer.get_all_by_name(name_pk)
        return JsonResponse({
            "code": HTTP_200_OK,
            "data": list(data.values())
        })
