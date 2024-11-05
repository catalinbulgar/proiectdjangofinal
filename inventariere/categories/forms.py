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

    def clean(self):
        name_value = self.cleaned_data.get('name')
        if Category.objects.filter(name__iexact=name_value).exists():
            self._errors['name'] = self.error_class(['Categoria deja existenta'])
        return self.cleaned_data
