from django.shortcuts import render
# from rest_framework import viewsets
from .serializers import StaffSerializer, CampSerializer, ProfileSerializer
from .models import Staff, Camp, Profile
# from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, status


# Create your views here.
class Home(APIView):

    def get(self, request):
        content = {'message': 'hello'}
        return JsonResponse(content)
    
    
    # ...............staff views............

class StaffView(APIView):
    def get(self, request):
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many = True)
        return Response(serializer.data)
    
    # .............camp views..............
    
class CampView(APIView):
    def get(self, request):
        queryset = Camp.objects.all()
        serializer = CampSerializer(queryset, many = True)
        return Response(serializer.data)
    
    # .......profile views................
    
class ProfileView(APIView):
    def get(self, request):
        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request):

    
    


