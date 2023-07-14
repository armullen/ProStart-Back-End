from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Camp(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    ageGroup = models.CharField(max_length=500)
    startDate = models.DateField(max_length=200)
    endDate = models.DateField(max_length=200)
    time = models.TimeField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    

class Staff(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    bio = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    name = models.CharField(max_length=200)
    athlete = models.CharField(max_length=200)
    sport = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['athlete']

    def __str__(self):
        return self.name
    
    