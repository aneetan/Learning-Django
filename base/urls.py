from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room_name/<str:pk>/', views.room, name='room'),
    path('create_room/', views.addRoom, name="addRoom"),
]