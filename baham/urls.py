from django.urls import path
from . import views

urlpatterns = [
      path('', views.view_home, name='home'),
      path('baham/aboutus', views.view_aboutus, name='aboutus'),
      path('baham/header', views.view_header, name='header'),
      path('bahm.fooetr', views.view_footer, name='footer')
]