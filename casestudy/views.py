from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def my_casestudy(request):
    return HttpResponse("Hello, blog!")