from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_index, name='meals'),
    path('edit/<int:id>', views.meal_edit, name='meal_edit'),
    path('delete/<int:id>', views.meal_delete, name='meal_delete'),
    path('ingredients', views.ingredient_index, name='ingredients'),
    path('ingredients/edit/<int:id>', views.ingredient_edit, name='ingredient_edit'),
    path('ingredients/delete/<int:id>', views.ingredient_delete, name='ingredient_delete')
]
