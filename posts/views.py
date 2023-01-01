from django.shortcuts import render
from django.http import HttpRequest , JsonResponse



def homepage(request):
    response = {'message':'my name is andrew'}
    return JsonResponse(data=response) 
    
# Create your views here.
