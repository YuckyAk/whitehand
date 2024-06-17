from .models import *
from django import forms


class Feedb(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'masage', 'number']

class CategoryFilterForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Категории"
    )

