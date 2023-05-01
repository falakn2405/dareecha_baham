from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request):
    return HttpResponse("<h1> Welcome to Baham </h1>")
