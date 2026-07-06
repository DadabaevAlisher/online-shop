from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email manzil")
    first_name = forms.CharField(required=True, max_length=30, label="Ism")
    last_name = forms.CharField(required=True, max_length=30, label="Familiya")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']