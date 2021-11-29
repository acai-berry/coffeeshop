from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Coffee

# Create your views here.

class CoffeeListView(ListView):
    model = Coffee
    template_name = 'coffee_list.html'


class CoffeeDetailView(DetailView):
    model = Coffee
    template_name = 'coffeeshop/coffee_detail.html'