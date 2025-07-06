from django.forms import ModelForm, TextInput, TimeInput
from meals.models import Ingredient, Meal


class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'healthiness']
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'healthiness': TimeInput(attrs={'type': 'number', 'min': 1, 'max': 5})
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'type': 'text'}),
            'servings': TimeInput(attrs={'type': 'number', 'value': 1}),
            'price': TextInput(attrs={'type': 'number', 'value': 0}),
            'url': TextInput(attrs={'type': 'url'})
        }
