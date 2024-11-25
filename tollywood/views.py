from django.shortcuts import render

from django.http import HttpResponse

def prabhas(request):
    return HttpResponse('<h1>prabhas is a hero of tollywood</h1>')

