from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def register(request):
    return HttpResponse("<h1>This is my register page</h1>")
def home(request):
    return HttpResponse("<h1>This is my home page</h1>")
def login(request):
    return HttpResponse("<h1>This is my login page</h1>")