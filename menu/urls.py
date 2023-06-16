from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<int:menu_item_id>/', views.menu_item_detail,
         name='menu_item_detail'),
    path('favourite/<int:menu_item_id>/', views.favourite_item,
         name='favourite_item'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('edit/<int:menu_item_id>/', views.edit_menu_item,
         name='edit_menu_item'),
    path('delete/<int:menu_item_id>/', views.delete_menu_item,
         name='delete_menu_item'),
]
