from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.home, name='home'),
    path('room_name/<str:pk>/', views.room, name='room'),
    path('create_room/', views.addRoom, name="addRoom"),
    path('edit_room/<str:key>/', views.editRoom, name="editRoom"),
    path('delete_room/<str:key>/', views.deleteRoom, name="deleteRoom"),
    path('deleteMsg/<str:key>/', views.deleteMessage, name="deleteMessage"),
    path('profile/<str:pk>', views.userProfile, name="userProfile"),



]