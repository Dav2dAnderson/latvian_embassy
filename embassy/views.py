from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions

from .models import Service, Meeting
from .serializers import ServiceSerializer, MeetingSerializer, MeetingDetailSerializer
from .permissons import IsAdminOrReadOnly


User = get_user_model()

# Create your views here.


""" ViewSet for Services """
class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'


""" ViewSet for Meeting management """
class MeetingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.filter(customer=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "create"]:
            return MeetingSerializer
        return MeetingDetailSerializer
        

