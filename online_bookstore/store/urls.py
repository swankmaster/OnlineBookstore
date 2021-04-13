from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('myCart/', views.myCart, name='myCart'),
    path('orderHistory/', views.orderHistory, name='orderHistory'),
    path('checkout/', views.myCart, name='checkout'),
    path('checkout/confirmation', views.checkoutConfirmation, name='checkoutConfirmation'),
    path('password_reset', views.password_reset, name='password_reset'),
    path('manage_promos', views.manage_promos, name='manage_promos'),
    path('manage_users', views.manage_users, name='manage_users'),
    path('manage_books', views.manage_books, name='manage_books'),
    path('suspended', auth_views.LogoutView.as_view(template_name='store/suspended.html'), name='suspended'),
]