from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, User1RegisterForm, UpdateUserInfoForm, UpdateUser1InfoForm, NewPasswordForm, CreditCardForm
from .models import Book, PaymentCard
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def home(request):
    context = {
        'books': Book.objects.all().exclude(quantity='0'),
        'coming_soon': Book.objects.all().filter(quantity='0')

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
        if 'infoSubmit' in request.POST:
            u_form = UpdateUserInfoForm(request.POST, instance=request.user)
            u1_form = UpdateUser1InfoForm(request.POST, instance=request.user.user1)
            p_form = NewPasswordForm()
            pay_form = CreditCardForm(instance=PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last())

            if u_form.is_valid() and u1_form.is_valid():
                u_form.save()
                u1_form.save()
                # send_mail(
                #     'Profile Information Changed',
                #     'Some of your profile information has been changed',
                #     '',
                #     ['to@example.com'],
                #     fail_silently=False,
                # )
        elif 'passSubmit' in request.POST:
            u_form = UpdateUserInfoForm(instance=request.user)
            u1_form = UpdateUser1InfoForm(instance=request.user.user1)
            p_form = NewPasswordForm(request.POST, instance=request.user)
            pay_form = CreditCardForm(instance=PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last())

            old_password = request.POST['old_password'].strip()

            user = request.user
            if old_password and p_form.is_valid():
                if user.check_password(old_password):
                    p_form.save()
                    messages.success(request, f'Password updated for {user.username}!')
                    return redirect('home')
                else:
                    messages.success(request, f'Password information is incorrect.')
            else:
                messages.success(request, f'Password information is incorrect.')
        elif 'paySubmit' in request.POST:
            pay_form = CreditCardForm(request.POST, instance=PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last())
            u_form = UpdateUserInfoForm(instance=request.user)
            u1_form = UpdateUser1InfoForm(instance=request.user.user1)
            p_form = NewPasswordForm()
            if pay_form.is_valid():
                if (PaymentCard.objects.all().filter(user1_user_id=request.user.user1)):
                    PaymentCard.objects.all().filter(user1_user_id=request.user.user1).last().delete()
                payment = pay_form.save(commit=False)
                # payment.card_number = PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last().card_number
                payment.user1_user_id = request.user.user1
                payment.save()

            # curr_pass = request.POST['curr_pass'].strip()
            # new_pass = request.POST['new_pass'].strip()
            # confirm_new_pass = request.POST['confirm_new_pass'].strip()
            #
            # if curr_pass and new_pass and confirm_new_pass == new_pass:
            #     user = request.user
            #     tempuser = User.objects.get(id=user.id)
            #     if user.check_password(curr_pass):
            #         tempuser.set_password(request.POST['new_pass'])
            #         tempuser.save()

    else:
        u_form = UpdateUserInfoForm(instance=request.user)
        u1_form = UpdateUser1InfoForm(instance=request.user.user1)
        p_form = NewPasswordForm()
        pay_form = CreditCardForm(instance=PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last())

    context = {
        'u_form': u_form,
        'u1_form': u1_form,
        'p_form': p_form,
        'pay_form': pay_form,
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

def password_reset(request):
    if request.method == 'POST':
        p_form = NewPasswordForm(request.POST)

        email = request.POST['email'].strip()
        old_password = request.POST['old_password'].strip()

        if email and old_password and p_form.is_valid():
            user = User.objects.all().filter(email=email).first()

            if user.check_password(old_password):
                user1 = p_form.save(commit=False)
                user1.username = user.username
                messages.success(request, f'Password updated for {user.username}!')
                return redirect('home')
            else:
                messages.success(request, f'Information is incorrect.')
        else:
            messages.success(request, f'Information is incorrect.')
    else:
        p_form = NewPasswordForm()

    context = {
        'p_form': p_form,
    }
    return render(request, 'store/password_reset.html', context)
