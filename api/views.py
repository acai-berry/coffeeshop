from django.contrib.auth import get_user_model
from rest_framework import viewsets
from coffeeshop.models import Coffee, Review
from .permissions import IsAuthorOrReadOnly
from .serializers import CoffeeSerializer, ReviewSerializer, UserSerializer

# Create your views here.

class CoffeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer