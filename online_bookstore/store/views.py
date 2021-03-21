from django.shortcuts import render
from django.http import HttpResponse

books = [
    {
        'img_src': 'PJTLT.jpg',
        'title': 'Percy Jackson: The Lightning Thief',
        'author': 'Rick Riordan',
        'price': '10',
        'description': 'Twelve-year-old Percy Jackson is on the most dangerous quest of his life. With the help of a satyr and a daughter of Athena, Percy must journey across the United States to catch a thief who has stolen the original weapon of mass destruction — Zeus’ master bolt. Along the way, he must face a host of mythological enemies determined to stop him. Most of all, he must come to terms with a father he has never known, and an Oracle that has warned him of betrayal by a friend.'
    },
    {
        'img_src': 'PJTSOFM.jpg',
        'title': 'Percy Jackson: Sea of Monsters',
        'author': 'Rick Riordan',
        'price': '10',
        'description': 'When Thalia’s tree is mysteriously poisoned, the magical borders of Camp Half-Blood begin to fail. Now Percy and his friends have just days to find the only magic item powerful to save the camp before it is overrun by monsters. The catch: they must sail into the Sea of Monsters to find it. Along the way, Percy must stage a daring rescue operation to save his old friend Grover, and he learns a terrible secret about his own family, which makes him question whether being the son of Poseidon is an honor or a curse.'
    },
    {
        'img_src': 'PJTTC.jpg',
        'title': 'Percy Jackson: The Titans Curse',
        'author': 'Rick Riordan',
        'price': '10',
        'description': 'When Percy Jackson gets an urgent distress call from his friend Grover, he immediately prepares for battle. He knows he will need his powerful demigod allies at his side, his trusty bronze sword Riptide, and… a ride from his mom.'
    },
    {
        'img_src': 'PJTBOTL.jpg',
        'title': 'Percy Jackson: The Battle of the Labyrinth',
        'author': 'Rick Riordan',
        'price': '10',
        'description': 'Percy Jackson isn’t expecting freshman orientation to be any fun, but when a mysterious mortal acquaintance appears, pursued by demon cheerleaders, things quickly go from bad to worse.'
    }

]

# Create your views here.
def home(request):
    context = {
        'books': books
    }
    return render(request, 'store/home.html', context)


def login(request):
    return render(request, 'store/login.html')


def edit_profile(request):
    return render(request, 'store/edit_profile.html')


def confirmation(request):
    return render(request, 'store/confirmation_page.html')
