from rest_framework import serializers;
from .models import Staff, Camp, Profile

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('name', 'img', 'bio')

class CampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camp
        fields = ('id', 'title', 'ageGroup', 'startDate', 'endDate', 'time', 'price')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'athlete', 'sport', 'position')