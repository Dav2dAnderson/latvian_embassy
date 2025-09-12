from dj_rest_auth.serializers import UserDetailsSerializer

from .models import CustomUser


class CustomUserDetailSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = UserDetailsSerializer.Meta.fields + (
            'phone_number',
        )
        read_only_fields = ('email', '')