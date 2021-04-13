from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget

from .models import User1, PaymentCard, Promotion, Book,Cart
from .fields import CreditCardField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (email == ""):
            raise forms.ValidationError('This field cannot be left blank')
        for instance in User.objects.all():
            if instance.email == email:
                raise forms.ValidationError(email + ' is already registered')
        return(email)

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']


        if commit:
            user.save()
        return user




class User1RegisterForm(forms.ModelForm):
    phone = forms.IntegerField(required=True)
    receive_promotions = forms.CheckboxInput()

    class Meta:
        model = User1
        fields = ('phone', 'receive_promotions')

        # widgets = {
        #     'phone': forms.TextInput(attrs={'class': 'form-control'}),
        #     'receive_promotions': forms.CheckboxInput(attrs={'class': 'form-control'}),
        # }


class UpdateUserInfoForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

class UpdateUser1InfoForm(forms.ModelForm):
    phone = forms.IntegerField()
    receive_promotions = forms.CheckboxInput()

    class Meta:
        model = User1
        fields = ('phone', 'receive_promotions')

class NewPasswordForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')

class CreditCardForm(forms.ModelForm):
    # TYPE_CHOICES = {
    #             ('Visa'),
    #             ('MasterCard'),
    #             ('Amex'),
    #             ('Paypal'),
    # }

    # type = forms.ChoiceField(choices=TYPE_CHOICES)
    card_number = forms.CharField()
    expiration_date = forms.CharField()
    cvv = forms.IntegerField(label='CVV')
    billing_address = forms.CharField()

    class Meta:
        model = PaymentCard
        fields = ('card_number','expiration_date','cvv', 'billing_address')


class NewPromoForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    end_date = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        )
    )
    discount = forms.IntegerField()

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if (end_date == ""):
            raise forms.ValidationError('This field cannot be left blank')
        if end_date <= start_date:
                raise forms.ValidationError('End date must be after the start date.')
        return(end_date)

    class Meta:
        model = Promotion
        fields = ('start_date', 'end_date', 'discount')

class SuspendUserForm(forms.Form):
    username = forms.CharField()

    class Meta:
        fields = ('username',)


class CreateBookForm(forms.ModelForm):
    title = forms.CharField(required=True)
    isbn = forms.CharField(required=True)
    author = forms.CharField(required=True)
    category = forms.CharField(required=True)
    description = forms.CharField(required=True)
    cover_picture = forms.ImageField()
    year = forms.IntegerField(required=True)
    buy_price = forms.FloatField(required=True)
    sell_price = forms.FloatField(required=True)
    edition = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True)
    rating = forms.FloatField(required=True)
    publisher = forms.CharField(required=True)
    minimum_threshold = forms.IntegerField(required=True)

    class Meta:
        model = Book
        fields = ("title","isbn","author","category","description","cover_picture","year","buy_price","sell_price","edition","quantity","rating","publisher","minimum_threshold")

    def __init__(self, *args, **kwargs):
        super(CreateBookForm, self).__init__(*args, **kwargs)
        self.fields['cover_picture'].required = False


    # card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)
    # expiration_date = forms.DateInput(format='%m/%y')
    # cvv = forms.IntegerField(label = 'CVV')
    #
    # class Meta:
    #     model = PaymentCard
    #     fields = ('card_number','expiration_date','cvv')

class AddToCartForm(forms.ModelForm):

    class Meta:
        model = Cart


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
