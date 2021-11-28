from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coffee(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    package = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=140)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
