from django.shortcuts import render
from .models import Room



# rooms = [
#     {'id' : 1, 'name' : "Python Django"},
#     {'id' : 2, 'name' : "UI/UX Design"},
#     {'id' : 3, 'name' : "Frontend Development"}

# ]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'r': rooms})

def room(request, pk):  
    room = Room.objects.get(id=pk)
    return render(request, 'room.html', {'room': room})
