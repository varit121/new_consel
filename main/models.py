from django.db import models

class City:
    name = models.TextField()
    latitude = models.FloatField()
    logitute = models.FloatField()
    founded = models.DateField()

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='habits')

class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    habits = models.ManyToManyField(Habit, related_name='challenges')
    tags = models.ManyToManyField(Tag, related_name='challenges')