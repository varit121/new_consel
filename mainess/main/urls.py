from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', views.get_cities, name='get_cities'),
    path('tags/', views.get_tags, name='get_tags'),
    path('habits/', views.get_habits, name='get_habits'),
    path('challenges/', views.get_challenges, name='get_challenges'),
    path('all/', views.get_all_data, name='get_all_data'),
]