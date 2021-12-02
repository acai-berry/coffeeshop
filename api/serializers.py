from django.contrib.auth import get_user_model
from rest_framework import serializers
from coffeeshop.models import Coffee, Review

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ('name', 'producer', 'origin', 'package')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('coffee', 'review', 'author', 'rating')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')