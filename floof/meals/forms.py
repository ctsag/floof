from django.forms import ModelForm, NumberInput, TextInput
from meals.models import Ingredient, Meal


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'healthiness']
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'healthiness': NumberInput(attrs={'type': 'number', 'step': 1, 'min': 1, 'max': 5})
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'servings': NumberInput(attrs={'type': 'number', 'step': 1}),
            'price': NumberInput(attrs={'type': 'number', 'step': 0.01}),
            'url': TextInput(attrs={'type': 'url'})
        }
