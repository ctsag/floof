from django.shortcuts import render
from planner.models import Meal, MealIngredient, Ingredient


def index(request):
    return render(
        request,
        'index.html',
        {
            'meals': Meal.objects.all(),
            'meal_ingredients': MealIngredient.objects.all(),
            'ingredients': Ingredient.objects.all()
        }
    )
