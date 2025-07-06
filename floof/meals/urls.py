from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_index, name='meals'),
    path('delete/<int:id>', views.meal_delete, name='meals_delete'),
    path('ingredients', views.ingredient_index, name='ingredients'),
    path('ingredients/delete/<int:id>', views.ingredient_delete, name='ingredients_delete')
]
