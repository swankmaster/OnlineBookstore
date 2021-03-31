from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, User1RegisterForm, UpdateUserInfoForm, UpdateUser1InfoForm, UpdateUserPassword
from .models import Book

# Create your views here.
def home(request):
    context = {
        'books': Book.objects.all()
    }

    return render(request, 'store/home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form1 = User1RegisterForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user1 = form1.save(commit=False)
            user1.user = user

            user1.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
        form1 = User1RegisterForm()
    return render(request, 'store/register.html', {'form': form, 'form1': form1})


def edit_profile(request):
    if request.method == 'POST':
        u_form = UpdateUserInfoForm(request.POST, instance=request.user)
        u1_form = UpdateUser1InfoForm(request.POST, instance=request.user.user1)
        if u_form.is_valid() and u1_form.is_valid():
            u_form.save()
            u1_form.save()

    else:
        u_form = UpdateUserInfoForm(instance=request.user)
        u1_form = UpdateUser1InfoForm(instance=request.user.user1)

    context = {
        'u_form': u_form,
        'u1_form': u1_form
    }
    return render(request, 'store/edit_profile.html', context)


def myCart(request):
    return render(request, 'store/myCart.html')

def orderHistory(request):
    return render(request, 'store/orderHistory.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def checkoutConfirmation(request):
    return render(request, 'store/checkoutConfirmation.html')


