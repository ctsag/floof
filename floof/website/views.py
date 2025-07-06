from django.shortcuts import render
from meals.models import Meal, Ingredient


def index(request):
    return render(
        request,
        'index.html',
        {
            'meal_count': Meal.objects.count(),
            'ingredient_count': Ingredient.objects.count()
        }
    )
