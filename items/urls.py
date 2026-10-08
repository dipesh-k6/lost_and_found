from django.urls import path
from . import views

urlpatterns = [
    path('submitfound/', views.FoundItemView.as_view(), name= 'submit_found_page'),
    path('reportlost/', views.LostItemView.as_view(), name= 'report_lost_page')
]