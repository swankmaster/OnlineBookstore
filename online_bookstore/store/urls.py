from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/confirmation/', views.confirmation, name='confirmation'),
]