from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    nme = request.GET['name']
    msg = request.GET['message']
    return HttpResponse('Hello {name}! {message}!'.format(name=nme, message=msg))



