from django.shortcuts import render
from menu.models import Ingredient, Meal


def index(request):
    return render(
        request,
        'index.html',
        {
            'meal_count': Meal.objects.count(),
            'ingredient_count': Ingredient.objects.count()
        }
    )
