from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('<int:room_id>/', views.room_detail, name='room_detail'),
    path('create/', views.room_create, name='room_create'),
    path('<int:room_id>/update/', views.room_update, name='room_update'),
    path('<int:room_id>/delete/', views.room_delete, name='room_delete'),
]