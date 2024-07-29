from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Room, Topic
from .forms import RoomForm


def loginPage(request):
    #getting values from frontend
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Incorrect username or password')


    context = {} 
    return render(request, 'base/login_register.html', context)


def home(request):
    #q is parameter from the url 
    # q = request.GET.get('q') if request.GET.get('q') != None else ''

    if request.GET.get('q') != None:
        q= request.GET.get('q')
        #icontains is case insensitive
        rooms = Room.objects.filter(
            Q(topic__name__icontains= q) |
            Q(name__icontains= q) |
            Q(description__icontains = q)
            )
    
    else:
        rooms = Room.objects.all()

    #search functionality
    topic = Topic.objects.all()

    room_count = rooms.count()

    context = {'r':rooms, 'topics': topic, 'room_count': room_count}

    return render(request, 'base/home.html', context)

def room(request, pk):  
    room = Room.objects.get(id=pk)
    return render(request, 'room.html', {'room': room})

def addRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form': form})

def editRoom(request, key):
    room = Room.objects.get(id = key)
    #the form will be filled with instance of room
    form = RoomForm(instance=room) 

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, key):
    room = Room.objects.get(id=key)

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':room})
