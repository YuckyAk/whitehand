from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from handmade.models import Product,Size


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    manufacturer = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Product
        fields = ['name','manufacturer','price','description']