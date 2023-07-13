from django.urls import path
from . import views

urlpatterns = [
    path('ourstaff/', views.StaffView.as_view(), name='staff_view'),
    path('', views.Home.as_view(), name='Home'),
    path('camps/', views.CampView.as_view(), name='camp_view'),
]