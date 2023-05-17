from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_home, name='home'),
    path('baham/vehicles', views.view_vehicles, name='vehicles'),
    path('baham/vehicles/create', views.create_vehicle, name='createvehicle'),
    path('baham/vehicles/save/', views.save_vehicle, name='savevehicle'),
    path('baham/vehicles/delete/<int:model_id>', views.delete_vehicle, name='deletevehicle'),
    path('baham/vehicles/undelete/<int:model_id>', views.undelete_vehicle, name='undeletevehicle'),
    path('baham/aboutus', views.view_aboutus, name='aboutus'),
]