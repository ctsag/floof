from django.shortcuts import render, redirect
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

def meal_delete(request, id):
    meal_id = id
    Meal.objects.get(id=meal_id).delete()
    return redirect(meal_index)

def ingredient_delete(request, id):
    ingredient_id = id
    Ingredient.objects.get(id=ingredient_id).delete()
    return redirect(ingredient_index)
