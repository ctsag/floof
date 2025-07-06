from django.contrib import admin
from meals.models import Meal, Ingredient, MealIngredient, PriceHistory

admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(MealIngredient)
admin.site.register(PriceHistory)
