from django.shortcuts import get_object_or_404, render, redirect
from meals.forms import IngredientForm, MealForm, MealIngredientForm
from meals.models import Ingredient, Meal, MealIngredient

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

def meal_view(request, id):
    meal = get_object_or_404(Meal, pk=id)

    return render(
        request,
        'meal_view.html',
        {
            'meal': meal
        }
    )

def ingredient_view(request, id):
    ingredient = get_object_or_404(Ingredient, pk=id)

    return render(
        request,
        'ingredient_view.html',
        {
            'ingredient': ingredient
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

def mealingredient_add(request, meal_id):
    if request.method == 'POST':
        form = MealIngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_view', id=meal_id)
    else:
        form = MealIngredientForm(initial={'meal': meal_id})

    return render(request, 'mealingredient_add.html', {'form': form, 'meal_id': meal_id})

def meal_edit(request, id):
    meal = get_object_or_404(Meal, pk=id)
    is_callback = request.GET.get('ref') == 'callback'

    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal_view', id=id) if is_callback else redirect('meals')
    else:
        form = MealForm(instance=meal)

    context = {'form': form, 'callback': id} if is_callback else {'form': form}
    return render(request, 'meal_edit.html', context)

def ingredient_edit(request, id):
    ingredient = get_object_or_404(Ingredient, pk=id)
    is_callback = request.GET.get('ref') == 'callback'

    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_view', id=id) if is_callback else redirect('ingredients')
    else:
        form = IngredientForm(instance=ingredient)

    context = {'form': form, 'callback': id} if is_callback else {'form': form}
    return render(request, 'ingredient_edit.html', context)

def mealingredient_edit(request, id):
    mealingredient = get_object_or_404(MealIngredient, pk=id)
    meal_id = mealingredient.meal.id

    if request.method == 'POST':
        form = MealIngredientForm(request.POST, instance=mealingredient)
        if form.is_valid():
            form.save()
            return redirect('meal_view', id=meal_id)
    else:
        form = MealIngredientForm(instance=mealingredient)

    return render(request, 'mealingredient_edit.html', {'form': form, 'meal_id': meal_id})

def meal_delete(request, id):
    meal = get_object_or_404(Meal, pk=id)
    meal.delete()

    return redirect(meal_index)

def ingredient_delete(request, id):
    ingredient = get_object_or_404(Ingredient, pk=id)
    ingredient.delete()

    return redirect(ingredient_index)

def mealingredient_delete(request, id):
    mealingredient = get_object_or_404(MealIngredient, pk=id)
    mealingredient.delete()

    return redirect(meal_view, id=mealingredient.meal.id)
