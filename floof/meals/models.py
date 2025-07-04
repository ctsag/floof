from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Ingredient(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=64)
    units = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    url = models.URLField(blank=True, null=True)

    objects = models.Manager()

    def unit_cost(self):
        return self.price / self.units

    def __str__(self):
        return f'{self.name}'

class Meal(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=128)
    healthiness = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    ingredients = models.ManyToManyField(Ingredient, through='MealIngredient')

    objects = models.Manager()

    def cost(self):
        return round(sum(item.cost() for item in self.mealingredient_set.all()), 2)

    def all_ingredients(self):
        return ', '.join(str(v) for v in self.mealingredient_set.all())

    def __str__(self):
        return f'{self.name} : {self.all_ingredients()} = {self.cost():.2f}€'

class MealIngredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    objects = models.Manager()

    def cost(self):
        return self.ingredient.unit_cost() * self.quantity

    def __str__(self):
        return f'{self.quantity}x {self.ingredient} @{self.cost():.2f}€'
