from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_Name = forms.CharField()
    last_Name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()


    class Meta:
        model = User
        fields = ['first_Name', 'last_Name', 'email', 'password1', 'password2', 'phone']
