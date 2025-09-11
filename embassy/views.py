from django.shortcuts import render

from rest_framework import viewsets

from .models import Service, Meeting
from .serializers import ServiceSerializer, MeetingSerializer
# Create your views here.


""" ViewSet for Services """
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'

        

""" ViewSet for Meeting management """
class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)