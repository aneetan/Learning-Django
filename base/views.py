from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'r': rooms})

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
