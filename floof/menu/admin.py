from django.contrib import admin
from menu.models import Ingredient, Meal, MealIngredient, PriceHistory

admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(MealIngredient)
admin.site.register(PriceHistory)
