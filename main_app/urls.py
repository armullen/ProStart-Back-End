from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('ourstaff/', views.StaffView.as_view(), name='staff_view'),
    path('camps/', views.CampView.as_view(), name='camp_view'),
    path('profile/', views.ProfileView.as_view(), name='profile_view'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profile_delete'),
    path('profile/<int:pk>/edit/', views.ProfileEdit.as_view(), name='profile_edit'),

]