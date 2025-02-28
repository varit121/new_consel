from django.shortcuts import render
from json import JSONEncoder
from django.http import *
from models import City
def cities(request:HttpRequest):
    if request.method == 'GET':
        city = City.objects().take(1)
        return JsonResponse(city,safe = False,encoder=JSONEncoder)
