from django.shortcuts import render
from meals.models import Meal, Ingredient


def index(request):
    return render(
        request,
        'index.html',
        {
            'meals': Meal.objects.all(),
            'ingredients': Ingredient.objects.all()
        }
    )
