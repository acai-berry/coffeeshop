from django.contrib import admin
from .models import Coffee, Review

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class CoffeeAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline
    ]

admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Review)
