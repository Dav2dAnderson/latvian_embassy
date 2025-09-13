from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers

from .models import CustomUser

from embassy.models import Meeting

class UserMeetingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ['id', 'service', 'meet_time', 'created_at']


class CustomUserDetailSerializer(UserDetailsSerializer):
    meetings = UserMeetingsSerializer(many=True, read_only=True)
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = UserDetailsSerializer.Meta.fields + (
            'phone_number',
            'meetings',
        )
        read_only_fields = ('email', '')


class CustomUserRegistrationSerializer(RegisterSerializer):
    phone_number = serializers.CharField(required=True, max_length=15)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['phone_number'] = self.validated_data.get('phone_number')
        return data
    
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        return user
    