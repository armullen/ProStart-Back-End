from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StaffSerializer
from .models import Staff
from django.views.generic.base import TemplateView
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response



# Create your views here.

class StaffView(APIView):
    def get(self, request):
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many = True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    
    
class Home(APIView):

    def get(self, request):
        content = {'message': 'hello'}
        return JsonResponse(content)


