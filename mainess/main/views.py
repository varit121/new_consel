from django.http import JsonResponse
from django.core.serializers import serialize
from .models import City, Tag, Habit, Challenge
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_cities(request):    
    cities = City.objects.all()
    cities_json = serialize('json', cities)
    return JsonResponse(cities_json, safe=False)


@require_http_methods(["GET"])
def get_tags(request):
    
    tags = Tag.objects.all()
    tags_json = serialize('json', tags)
    return JsonResponse(tags_json, safe=False)


@require_http_methods(["GET"])
def get_habits(request):
    
    habits = Habit.objects.all()
    habits_json = serialize('json', habits)
    return JsonResponse(habits_json, safe=False)


@require_http_methods(["GET"])
def get_challenges(request):
   
    challenges = Challenge.objects.all()
    challenges_json = serialize('json', challenges)
    return JsonResponse(challenges_json, safe=False)