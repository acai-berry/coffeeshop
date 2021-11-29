from django.urls import path
from .views import CoffeeDetailView, CoffeeListView


urlpatterns = [
    path('', CoffeeListView.as_view(), name='home'),
    path('<int:pk>/', CoffeeDetailView.as_view(), name='coffee_detail'),
]