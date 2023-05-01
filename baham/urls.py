from django.urls import path
from . import views

urlpatterns = [
      path('', views.view_home, name='home'),
      path('baham/aboutus', views.view_aboutus, name='aboutus')
]