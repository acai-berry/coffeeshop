from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from .views import UserViewSet, CoffeeViewSet, ReviewViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('coffee', CoffeeViewSet, basename='coffee')


coffee_router = routers.NestedDefaultRouter(router, 'coffee', lookup='coffee')
coffee_router.register('reviews', ReviewViewSet, basename='coffee-reviews')

urlpatterns = router.urls + coffee_router.urls
