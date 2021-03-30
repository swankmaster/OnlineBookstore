from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('myCart/', views.edit_profile, name='myCart'),
    path('orderHistory/', views.edit_profile, name='orderHistory'),
]