from django.forms import ModelForm, NumberInput, Select, TextInput
from menu.models import Ingredient, Meal, MealIngredient


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'slot_type', 'healthiness']
        labels = {'slot_type': 'Type'}
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'slot_type': Select(attrs={'required': 'true'}),
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


class MealIngredientForm(ModelForm):
    class Meta:
        model = MealIngredient
        fields = '__all__'
        widgets = {
            'meal': Select(attrs={'required': 'true'}),
            'ingredient': Select(attrs={'required': 'true'}),
            'quantity': NumberInput(attrs={'type': 'number', 'step': 1})
        }
