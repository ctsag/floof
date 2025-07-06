from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_index, name='meals'),
    path('ingredients', views.ingredient_index, name='ingredients')
]
