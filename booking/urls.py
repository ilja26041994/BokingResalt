from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_booking, name="addBooking"),
    path('info/', views.get_basket, name="getBasket"),
    path('delete/', views.delete_booking, name="deleteBooking"),
    path('addBasket/', views.add_to_basket, name="addBasket"),
]