from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def nomPage(request):
    return HttpResponse('<h1> Ahla b si Iheb</h1>')