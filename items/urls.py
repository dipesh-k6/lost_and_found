from django.urls import path
from . import views

urlpatterns = [
    path('submitfound/', views.FoundItemView.as_view(), name= 'submit_found_page'),
    path('reportlost/', views.LostItemView.as_view(), name= 'report_lost_page'),
    path('edit/<int:item_id>', views.EditItem.as_view(), name='edit_item_page'),
    path('delete/<int:item_id>', views.DeleteItem.as_view(), name='delete_item_page')
]