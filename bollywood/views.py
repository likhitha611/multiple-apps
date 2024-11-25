from django.shortcuts import render

from django.http import HttpResponse

def ranbir(request):
    return HttpResponse('<h1>ranbir is a hero of bollywood</h1>')
