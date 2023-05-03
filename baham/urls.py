from django.urls import path
from . import views

urlpatterns = [
      path('', views.view_home, name='home'),
      path('baham/vehicles/', views.view_vehicles, name='vehicles'),
      path('baham/vehicles/create/', views.create_vehicle, name='create_vehicle'),
      
      path('baham/aboutus', views.view_aboutus, name='aboutus'),
]