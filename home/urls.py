from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact_us/', views.customer_contact, name='contact_us'),
]
