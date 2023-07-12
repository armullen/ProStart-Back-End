from django.db import models

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