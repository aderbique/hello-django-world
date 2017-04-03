from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.


def index(request):
    now = time.strftime("%c")
    html = "<html><body><h1>Hello, World. It is now %s.</h1> <style> body{background-color: #ADD8E6} h1{text-align: center;} </style> </body></html>" % now
    return HttpResponse(html)
