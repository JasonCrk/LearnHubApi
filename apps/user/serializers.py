from rest_framework.serializers import ModelSerializer

from djoser.serializers import UserCreateSerializer, get_user_model

User = get_user_model()


class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'get_full_name',
        )


class UserAccountCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
        )
