from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def arjun(request):
    return HttpResponse('<h1>arjun is a hero of hollywood</h1>')
