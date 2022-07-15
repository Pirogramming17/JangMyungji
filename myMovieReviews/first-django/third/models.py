from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=10)
    point = models.CharField(max_length=1)
    running_time = models.CharField(max_length=3)
    review = models.CharField(max_length=500)
    producer = models.CharField(max_length=30)
    actor = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)
