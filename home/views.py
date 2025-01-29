from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hey I'm  a django developer")

def success_page(request):
    return HttpResponse('This is a success page')