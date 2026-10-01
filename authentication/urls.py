from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_user, name = 'signup_page'),
    path('login/', views.login_user, name= 'login_page'),
    path('logout/', views.logout_user, name= 'logout_page')
]