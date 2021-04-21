from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, User1RegisterForm, UpdateUserInfoForm, UpdateUser1InfoForm, NewPasswordForm, CreditCardForm, NewPromoForm, SuspendUserForm, CreateBookForm
from .models import Book, PaymentCard, Promotion, User1
from django.contrib.auth.models import User
from online_bookstore.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import datetime
from django.utils import timezone

# Create your views here.
def home(request):
    books = [
        [1, 'Percy Jackson: The Lightning Thief', '', 'Rick Riordan', 'Fiction',
        "Twelve-year-old Percy Jackson is on the most dangerous quest of his life. With the help of a satyr and a daughter of Athena, Percy must journey across the United States to catch a thief who has stolen the original weapon of mass destruction — Zeus’ master bolt. Along the way, he must face a host of mythological enemies determined to stop him. Most of all, he must come to terms with a father he has never known, and an Oracle that has warned him of betrayal by a friend.",
        'PJTLT.jpg', '2005', '8', '10', '2', '2000', '4.7', 'Puffin', '20'],
        [2, 'Percy Jackson: Sea of Monsters', ' ', 'Rick Riordan', 'Fiction',
        "When Thalia’s tree is mysteriously poisoned, the magical borders of Camp Half-Blood begin to fail. Now Percy and his friends have just days to find the only magic item powerful to save the camp before it is overrun by monsters. The catch: they must sail into the Sea of Monsters to find it. Along the way, Percy must stage a daring rescue operation to save his old friend Grover, and he learns a terrible secret about his own family, which makes him question whether being the son of Poseidon is an honor or a curse.",
        'PJTSOFM.jpg', '2007', '8', '10', '2', '150', '4.2', 'Puffin', '20'],
        [3, 'Percy Jackson: The Titans Curse', ' ', 'Rick Riordan', 'Fiction',
        "When Percy Jackson gets an urgent distress call from his friend Grover, he immediately prepares for battle. He knows he will need his powerful demigod allies at his side, his trusty bronze sword Riptide, and… a ride from his mom.",
        'PJTTC.jpg', '2008', '8', '10', '2', '124', '4.6', 'Puffin', '20'],
        [4, 'Percy Jackson: The Battle of the Labyrinth', ' ', 'Rick Riordan', 'Fiction',
        "Percy Jackson isn’t expecting freshman orientation to be any fun, but when a mysterious mortal acquaintance appears, pursued by demon cheerleaders, things quickly go from bad to worse.",
        'PJTBOTL.jpg', '2010', '8', '10', '2', '140', '4.9', 'Puffin', '20'],
        [5, 'Harry Potter and The Sorcerer\'s Stone', ' ', 'JK Rowling', 'Fiction',
        "At the beginning of the novel, Harry Potter is living in a cupboard under the stairs, suffering appalling maltreatment at the hands of the Dursley family, to whose care he was confided as an infant following the death of his parents; his mother was Mrs. Dursley’s sister. On his eleventh birthday, however, it is revealed to him, despite the Dursleys’ best efforts, that he has inherited magical abilities and is scheduled for education in wizardry at Hogwarts Academy, a key pillar of the British magical community, which lives in strict covert isolation from untalented “muggles.” This message is delivered by the intimidating Hagrid, who lives on the school grounds on the edge of a Forbidden Forest. Hagrid, who is fascinated by all manner of magical creatures, becomes Harry’s first fast friend.",
        'HPTSS.jpg', '1997', '8', '15', '2', '0', '4.9', 'Puffin', '20'],
        [6, 'Harry Potter and the Chamber of Secrets', ' ', 'JK Rowling', 'Fiction',
        "It's year two at Hogwarts, and Harry, Ron, and Hermione are back learning, but their year doesn't go passed quietly. Members of the school are turning up petrified and bloody writings are appearing on the walls, revealing to everyone, that someone has opened the Chamber of Secrets. The attacks continue, bringing the possibility of the closure of Hogwarts. Harry and his friends are now forced to secretly uncover the truth about the chamber before the school closes or any lives are taken.",
        'HPTCOS.jpg', '1999', '8', '15', '2', '0', '4.9', 'Puffin', '20'],
        [7, 'Harry Potter and the Prisoner of Azkaban', ' ', 'JK Rowling', 'Fiction',
        "Harry Potter, Ron and Hermione return to Hogwarts School of Witchcraft and Wizardry for their third year of study, where they delve into the mystery surrounding an escaped prisoner who poses a dangerous threat to the young wizard.",
        'HPPOA.jpg', '2001', '8', '15', '2', '0', '4.9', 'Puffin', '20'],
        [8, 'Harry Potter and the Goblet of Fire', ' ', 'JK Rowling', 'Fiction',
        "The Tri-Wizard Tournament is open. Four champions are selected to compete in three terrifying tasks in order to win the Tri-Wizard Cup. Meanwhile, Harry Potter is selected by the Goblet of Fire to compete while struggling to keep up the pace with classes and friends. He must confront fierce dragons, aggressive mermaids, and a dark wizard that hasn't been able to make his move for thirteen years.",
        'HPGOF.jpg', '2004', '8', '15', '2', '0', '4.9', 'Puffin', '20'],
    ]
    if not Book.objects.all():
        for book in books:
            b = Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7], book[8], book[9], book[10], book[11], book[12], book[13], book[14])
            b.save()
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
            email = form.cleaned_data.get('email')

            messages.success(request, f'Account created for {username}!')

            subject = 'New User Created!'
            message = 'Congratulations ' + username + '! You have created a new account.'

            print('recipient: ' + email + '\nHOST_USER: ' + EMAIL_HOST_USER)
            send_mail(subject, message, EMAIL_HOST_USER, [email], fail_silently= False)

            return redirect('home')
    else:
        form = UserRegisterForm()
        form1 = User1RegisterForm()
    return render(request, 'store/register.html', {'form': form, 'form1': form1})


def edit_profile(request):
    too_many = False
    if request.method == 'POST':
        if 'infoSubmit' in request.POST:
            u_form = UpdateUserInfoForm(request.POST, instance=request.user)
            u1_form = UpdateUser1InfoForm(request.POST, instance=request.user.user1)
            p_form = NewPasswordForm()
            pay_form = CreditCardForm(instance=PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last())

            if u_form.is_valid() and u1_form.is_valid():
                u_form.save()
                u1_form.save()
                return redirect('edit_profile')
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
                    return redirect('edit_profile')
                else:
                    messages.success(request, f'Password information is incorrect.')
            else:
                messages.success(request, f'Password information is incorrect.')
        elif 'paySubmit' in request.POST:
            pay_form = CreditCardForm(request.POST)
            u_form = UpdateUserInfoForm(instance=request.user)
            u1_form = UpdateUser1InfoForm(instance=request.user.user1)
            p_form = NewPasswordForm()
            cards = PaymentCard.objects.all().filter(user1_user_id=request.user.user1)

            if pay_form.is_valid():
                if len(PaymentCard.objects.all().filter(user1_user_id=request.user.user1)) < 3:
                    payment = pay_form.save(commit=False)
                    payment.user1_user_id = request.user.user1
                    payment.save()
                    return redirect('edit_profile')
                else:
                    too_many = True

                # if (PaymentCard.objects.all().filter(user1_user_id=request.user.user1)):
                #     PaymentCard.objects.all().filter(user1_user_id=request.user.user1).last().delete()
                # payment = pay_form.save(commit=False)
                # # payment.card_number = PaymentCard.objects.all().filter(user1_user_id = request.user.user1).last().card_number
                # payment.user1_user_id = request.user.user1
                # payment.save()

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

        elif 'delete' in request.POST:
            pay_form = CreditCardForm()
            u_form = UpdateUserInfoForm(instance=request.user)
            u1_form = UpdateUser1InfoForm(instance=request.user.user1)
            p_form = NewPasswordForm()

            id = request.POST['delete']
            if PaymentCard.objects.all().filter(card_id=id):
                PaymentCard.objects.all().filter(card_id=id).first().delete()

            cards = PaymentCard.objects.all().filter(user1_user_id=request.user.user1)
            return redirect('edit_profile')
    else:
        u_form = UpdateUserInfoForm(instance=request.user)
        u1_form = UpdateUser1InfoForm(instance=request.user.user1)
        p_form = NewPasswordForm()
        pay_form = CreditCardForm()
        cards = PaymentCard.objects.all().filter(user1_user_id = request.user.user1)

    context = {
        'u_form': u_form,
        'u1_form': u1_form,
        'p_form': p_form,
        'pay_form': pay_form,
        'cards': cards,
        'too_many': too_many,
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

def suspended(request):
    return render(request, 'store/suspended.html')

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

def manage_promos(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            p_form = NewPromoForm()
            id = request.POST['delete']
            if Promotion.objects.all().filter(promo_id = id):
                promo = Promotion.objects.all().filter(promo_id = id).first().delete()
        else:
            p_form = NewPromoForm(request.POST)
            if p_form.is_valid():
                p_form.save()

                messages.success(request, f'New Promo Created.')

                recipient_list = User1.objects.all().filter(receive_promotions = True)
                email_list = [User.objects.all().filter(username = i.user).first().email for i in recipient_list]

                subject = 'New Promo!'
                message = 'You have received a new promo for ' + request.POST['discount'] + '% off'

                # print('recipient: ' + email_list + '\nHOST_USER: ' + EMAIL_HOST_USER)

                send_mail(subject, message, EMAIL_HOST_USER, email_list, fail_silently=False)

                return redirect('manage_promos')
    else:
        p_form = NewPromoForm()

    promos = Promotion.objects.all()
    active_promos = []
    inactive_promos = []
    now = timezone.now()

    for i in promos:
        if i.end_date > now:
            active_promos.append(i)
        else:
            inactive_promos.append(i)


    context = {
        'p_form': p_form,
        'active_promos': active_promos,
        'inactive_promos': inactive_promos,
        'now': now,
    }
    return render(request, 'store/manage_promos.html', context)


def manage_books(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():

            book = form.save(commit=False)
            book.cover_picture = request.POST['cover_picture']
            book.save()

            messages.success(request, f'New Book Created.')

            recipient_list = User1.objects.all().filter(receive_promotions = True)
            email_list = [User.objects.all().filter(username = i.user).first().email for i in recipient_list]

            subject = 'New Book Added!'
            message = 'We have just added a new book: ' + request.POST['title']

            send_mail(subject, message, EMAIL_HOST_USER, email_list, fail_silently=False)

            return redirect('manage_books')
    else:
        form = CreateBookForm()

    context = {
        'form': form,
        'books': Book.objects.all(),
    }
    return render(request, 'store/manage_books.html', context)


def manage_users(request):
    if request.method == 'POST':
        form = SuspendUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            if User.objects.all().filter(username = username):
                user = User.objects.all().filter(username = username).first()
                if 'suspend' in request.POST:
                    user.user1.user_suspend = not user.user1.user_suspend
                    user.user1.save()
                    if(user.user1.user_suspend):
                        messages.success(request, f'{user.username} has been suspended.')
                    else:
                        messages.success(request, f'{user.username} has been unsuspended.')
                elif 'employee' in request.POST:
                    user.is_staff = not user.is_staff
                    user.save()
                    if (user.is_staff):
                        messages.success(request, f'Employee permissions given to: {user.username}')
                    else:
                        messages.success(request, f'Employee permissions removed from: {user.username}')
                elif 'admin' in request.POST:
                    user.is_superuser = not user.is_superuser
                    user.save()
                    if (user.is_superuser):
                        messages.success(request, f'Admin permissions given to: {user.username}')
                    else:
                        messages.success(request, f'Admin permissions removed from: {user.username}')
            else:
                messages.success(request, f'Invalid Username.')


            return redirect('manage_users')
    else:
        form = SuspendUserForm()

    context = {
        'form' : form,
        'users' : User.objects.all()
    }
    return render(request, 'store/manage_users.html', context)


