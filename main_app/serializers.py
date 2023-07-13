from rest_framework import serializers;
from .models import Staff, Camp

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('name', 'img', 'bio')

class CampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camp
        fields = ('title', 'ageGroup', 'startDate', 'endDate', 'time', 'price')