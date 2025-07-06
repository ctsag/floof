from django.shortcuts import get_object_or_404, render, redirect
from meals.forms import IngredientForm, MealForm
from meals.models import Ingredient, Meal

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

def meal_add(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals')
    else:
        form = MealForm()

    return render(request, 'meal_add.html', {'form': form})

def ingredient_add(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredients')
    else:
        form = IngredientForm()

    return render(request, 'ingredient_add.html', {'form': form})

def meal_edit(request, id):
    meal = get_object_or_404(Meal, pk=id)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meals')
    else:
        form = MealForm(instance=meal)

    return render(request, 'meal_edit.html', {'form': form})

def ingredient_edit(request, id):
    ingredient = get_object_or_404(Ingredient, pk=id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredients')
    else:
        form = IngredientForm(instance=ingredient)

    return render(request, 'ingredient_edit.html', {'form': form})

def meal_delete(request, id):
    meal = get_object_or_404(Meal, pk=id)
    meal.delete()
    return redirect(meal_index)

def ingredient_delete(request, id):
    ingredient = get_object_or_404(Ingredient, pk=id)
    ingredient.delete()
    return redirect(ingredient_index)
