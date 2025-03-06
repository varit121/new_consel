from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cities/', views.get_cities, name='get_cities'),
    path('api/tags/', views.get_tags, name='get_tags'),
    path('api/habits/', views.get_habits, name='get_habits'),
    path('api/challenges/', views.get_challenges, name='get_challenges'),
]