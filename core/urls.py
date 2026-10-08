from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name= 'dashboard_page'),
    path('<str:username>/<int:userid>', views.user_page, name= 'user_page')
]