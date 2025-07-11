from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from schedule.models import SlotType


class Ingredient(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=64)
    servings = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    url = models.URLField(blank=True, null=True)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if self.pk:
            prev_price = Ingredient.objects.get(pk=self.pk).price
            if prev_price != self.price:
                PriceHistory.objects.create(
                    ingredient=self,
                    prev_price=prev_price,
                    new_price=self.price
                )
        super().save(*args, **kwargs)

    def unit_cost(self):
        return self.price / self.servings

    def __str__(self):
        return f'{self.name}'


class PriceHistory(models.Model):
    class Meta:
        verbose_name_plural = 'price history'

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    prev_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    new_price = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    changed_at = models.DateTimeField(auto_now=True)

    def formatted_change_date(self):
        return self.changed_at.strftime('%B %d, %Y %H:%M:%S')

    def __str__(self):
        return f"""{self.ingredient} from {self.prev_price} to {self.new_price}
        at {self.formatted_change_date()}"""


class Meal(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=128)
    slot_type = models.ForeignKey(SlotType, on_delete=models.CASCADE)
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
        return round(self.ingredient.unit_cost() * self.quantity, 2)

    def __str__(self):
        return f'{self.quantity}x {self.ingredient} @{self.cost():.2f}€'
