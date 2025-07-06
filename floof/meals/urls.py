from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_index, name='meals'),
    path('<int:id>', views.meal_view, name='meal_view'),
    path('add', views.meal_add, name='meal_add'),
    path('edit/<int:id>', views.meal_edit, name='meal_edit'),
    path('delete/<int:id>', views.meal_delete, name='meal_delete'),
    path('ingredients', views.ingredient_index, name='ingredients'),
    path('ingredients/<int:id>', views.ingredient_view, name='ingredient_view'),
    path('ingredients/add', views.ingredient_add, name='ingredient_add'),
    path('ingredients/edit/<int:id>', views.ingredient_edit, name='ingredient_edit'),
    path('ingredients/delete/<int:id>', views.ingredient_delete, name='ingredient_delete')
]
