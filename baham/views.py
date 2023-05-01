from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader

# Create your views here.
def view_home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

# Create your views here.
def view_aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render({}, request))

# Create your views here.
def view_header(request):
    template = loader.get_template('header.html')
    return HttpResponse(template.render({}, request))

# Create your views here.
def view_footer(request):
    template = loader.get_template('footer.html')
    return HttpResponse(template.render({}, request))
