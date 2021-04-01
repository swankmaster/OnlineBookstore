from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .fields import CreditCardField
from .models import User1, PaymentCard
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class User1RegisterForm(forms.ModelForm):
    phone = forms.IntegerField()

    class Meta:
        model = User1
        fields = ('phone',)

class UpdateUserInfoForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class UpdateUser1InfoForm(forms.ModelForm):
    phone = forms.IntegerField()

    class Meta:
        model = User1
        fields = ('phone',)

class UpdateUserPassword(forms.ModelForm):
    old_password = forms.PasswordInput()
    password = forms.PasswordInput()

    class Meta:
        model = User
        exclude = ('old_password',)
        fields = ('old_password', 'password')

class CreditCardForm(forms.ModelForm):
    card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)
    expiration_date = forms.DateInput(format='%m/%y')
    cvv = forms.IntegerField(label = 'CVV')

    class Meta:
        model = PaymentCard
        fields = ('card_number','expiration_date','cvv')

# class UpdatePaymentInfoForm(forms.ModelForm):
#     TYPE_CHOICES = (
#         ('Visa'),
#         ('MasterCard'),
#         ('Amex'),
#         ('Paypal'),
#     )
#     type = forms.ChoiceField(choices=TYPE_CHOICES)
#     card_num = forms.IntegerField(label='Card Number:')
#     exp_date = forms.DateField(label='Expiration Data')
#     cvv = forms.IntegerField(label='CVV')
#
#     class Meta:
#         model = PaymentCard
#         fields = ('first_name', 'last_name', 'username', 'email', 'password')
