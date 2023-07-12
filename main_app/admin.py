from django.contrib import admin
from .models import Camp

# Register your models here.

class CampAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ageGroup', 'startDate', 'endDate', 'time', 'price')

admin.site.register(Camp, CampAdmin)