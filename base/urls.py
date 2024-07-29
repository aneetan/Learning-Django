from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('', views.home, name='home'),
    path('room_name/<str:pk>/', views.room, name='room'),
    path('create_room/', views.addRoom, name="addRoom"),
    path('edit_room/<str:key>/', views.editRoom, name="editRoom"),
    path('delete_room/<str:key>/', views.deleteRoom, name="deleteRoom"),


]