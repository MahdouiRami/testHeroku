from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


def nomPage(request):
    return HttpResponse('<h1> Ahla b si Iheb</h1>')

class ListUsers(APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        
        return Response("ahla Rami")