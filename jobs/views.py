from django.shortcuts import render
from django.http import HttpResponse
def Index(request):
    return HttpResponse('<h1>welcome to the app</h1>')

