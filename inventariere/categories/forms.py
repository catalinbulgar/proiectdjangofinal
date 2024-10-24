from django import forms
from django.forms import TextInput

from categories.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'name', 'class': 'form-class'}),
        }
