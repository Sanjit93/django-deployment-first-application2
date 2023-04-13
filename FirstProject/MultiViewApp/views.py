from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def f1(request):
    return HttpResponse("<h2>Good morning User...!!!</h1><hr/>");
def f2(request):
    return HttpResponse("<h2>Good afternoon User...!!!</h1><hr/>");
def f3(request):
    return HttpResponse("<h2>Good Evening User...!!!</h1><hr/>");