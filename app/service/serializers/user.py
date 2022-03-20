from rest_framework.serializers import ModelSerializer

from service.models.user import User


class UserSerializer(ModelSerializer):
    """
    User Serializer
    """
    queryset = User.objects.all()

    @classmethod
    def get_all_by_name(cls, name: str):
        return User.objects.filter(name=name).all()

    class Meta:
        model = User
        fields = [
            'name',
            'age'
        ]
