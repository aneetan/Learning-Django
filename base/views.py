from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Room, Topic,Message
from .forms import RoomForm


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    #getting values from frontend
    if request.method == 'POST':
        username = request.POST.get('username').lower()
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


    context = {'page':page} 
    return render(request, 'base/login_register.html', context)

def registerUser(request):
    page = 'register'

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #commit False to get that user instantly
            user = form.save(commit=False)

            #clean data
            user.username = user.username.lower()
            user.save()

            #send the user to home page with loeed in status
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Error occured')

    return render(request, 'base\login_register.html', {'form': form })


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

    #give us set of messages that are related to this room
    message = room.message_set.all().order_by('-created')

    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )

        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room': room, 'msg': message, 'participants': participants}
    return render(request, 'room.html', context )

@login_required(login_url='login')
def addRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', {'form': form})

@login_required(login_url='login')
def editRoom(request, key):
    room = Room.objects.get(id = key)
    #the form will be filled with instance of room
    form = RoomForm(instance=room) 

    #to edit only the room of logged user
    if request.user != room.host:
        return HttpResponse('Permission denied')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, key):
    room = Room.objects.get(id=key)

    if request.user != room.host:
        return HttpResponse('Permission denied')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':room})


@login_required(login_url='login')
def deleteMessage(request, key):
    message = Message.objects.get(id=key)

    if request.user != message.user:
        return HttpResponse('Permission denied')

    if request.method == 'POST':
        message.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj':message})


def logoutUser(request):
    logout(request)
    return redirect('home')