from django.http import JsonResponse
from django.urls import reverse  # Для генерации ссылок
from .models import City, Tag, Habit, Challenge
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_cities(request):
    cities = list(City.objects.values())
    return JsonResponse({
        "data": cities,
        "links": {
            "self": request.build_absolute_uri(),
            "rel": request.build_absolute_uri(reverse('get_all_data'))  
        }
    })

@require_http_methods(["GET"])
def get_tags(request):
    tags = list(Tag.objects.values())
    return JsonResponse({
        "data": tags,
        "links": {
            "self": request.build_absolute_uri(),
            "rel": request.build_absolute_uri(reverse('get_all_data'))  
        }
    })

@require_http_methods(["GET"])
def get_habits(request):
    habits = list(Habit.objects.values())
    return JsonResponse({
        "data": habits,
        "links": {
            "self": request.build_absolute_uri(),
            "rel": request.build_absolute_uri(reverse('get_all_data')) 
        }
    })

@require_http_methods(["GET"])
def get_challenges(request):
    challenges = list(Challenge.objects.values())
    return JsonResponse({
        "data": challenges,
        "links": {
            "self": request.build_absolute_uri(),
            "rel": request.build_absolute_uri(reverse('get_all_data')) 
        }
    })

@require_http_methods(["GET"])
def get_all_data(request):
    return JsonResponse({
        "data": {
            "cities": list(City.objects.values()),
            "tags": list(Tag.objects.values()),
            "habits": list(Habit.objects.values()),
            "challenges": list(Challenge.objects.values())
        },
        "links": {
            "self": request.build_absolute_uri(),
            "rel": {  
                "cities": request.build_absolute_uri(reverse('get_cities')),
                "tags": request.build_absolute_uri(reverse('get_tags')),
                "habits": request.build_absolute_uri(reverse('get_habits')),
                "challenges": request.build_absolute_uri(reverse('get_challenges'))
            }
        }
    })