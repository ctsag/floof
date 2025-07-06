from django.shortcuts import render
from meals.models import Meal, Ingredient


def meal_index(request):
    return render(
        request,
        'meals.html',
        {
            'meals': Meal.objects.all()
        }
    )

def ingredient_index(request):
    return render(
        request,
        'ingredients.html',
        {
            'ingredients': Ingredient.objects.all()
        }
    )
