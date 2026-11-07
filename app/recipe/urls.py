"""
URL mappings for the recipe API.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipe import views

app_name = 'recipe'

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet, basename='recipe')

urlpatterns = [
    path('', include(router.urls)),
]