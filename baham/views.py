from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

# Create your views here.
def view_home(request):
    template = loader.get_template('home.html')
    context = {
        "navbar": "home"
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def view_aboutus(request):
    template = loader.get_template('aboutus.html')
    context = {
        "navbar": "aboutus"
    }
    return HttpResponse(template.render(context, request))
