from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StaffSerializer
from .models import Staff

# Create your views here.

class StaffView(viewsets.ReadOnlyModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    
