from django.contrib import admin
from meals.models import Meal, Ingredient, MealIngredient

admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(MealIngredient)
