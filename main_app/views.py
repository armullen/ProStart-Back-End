from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StaffSerializer, CampSerializer
from .models import Staff, Camp
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response



# Create your views here.

class StaffView(APIView):
    def get(self, request):
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many = True)
        return Response(serializer.data)
    
class CampView(APIView):
    def get(self, request):
        queryset = Camp.objects.all()
        serializer = CampSerializer(queryset, many = True)
        return Response(serializer.data)

    
    
class Home(APIView):

    def get(self, request):
        content = {'message': 'hello'}
        return JsonResponse(content)


