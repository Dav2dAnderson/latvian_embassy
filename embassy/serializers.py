from rest_framework import serializers

from accounts.models import CustomUser

from .models import Meeting, Service


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'slug']


class MeetingSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())
    class Meta:
        model = Meeting
        fields = ['id', 'customer', 'service', 'meet_time']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['customer'] = CustomUserSerializer(instance.customer).data
        rep['service'] = ServiceSerializer(instance.service).data
        return rep


class MeetingDetailSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(read_only=True)
    customer = CustomUserSerializer(read_only=True)
    class Meta:
        model = Meeting
        fields = ['id', 'customer', 'meet_time', 'service', 'created_at']