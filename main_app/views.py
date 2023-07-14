from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StaffSerializer, CampSerializer, ProfileSerializer
from .models import Staff, Camp, Profile
# from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response



# Create your views here.
class Home(APIView):

    def get(self, request):
        content = {'message': 'hello'}
        return JsonResponse(content)

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
    
class ProfileView(APIView):
    def get(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many = True)
        return Response(serializer.data)

    
    


