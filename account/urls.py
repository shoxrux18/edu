from django.urls import path
from .views import account_login,account_register,portfolio,profile,membership,forget_password
from .views import account_logout
app_name = 'account'
urlpatterns = [
    path('login/',account_login,name='login'),
    path('register/',account_register,name='register'),
    path('portfolio/',portfolio,name='portfolio'),
    path('profile/',profile,name='profile'),
    path('membership/',membership,name='membership'),
    path('forget_password/',forget_password,name='forget_password'),
    path('logout/',account_logout,name='logout')
]