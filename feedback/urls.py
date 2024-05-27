from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_ticket, name='create_ticket'),
    path('', views.feedback_list, name='feedback_list'),
    path('<int:id>/', views.feedback_detail, name='feedback_detail'),
]