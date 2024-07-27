from django.shortcuts import render



rooms = [
    {'id' : 1, 'name' : "Python Django"},
    {'id' : 2, 'name' : "UI/UX Design"},
    {'id' : 3, 'name' : "Frontend Development"}

]

def home(request):
    return render(request, 'base/home.html', {'r': rooms})

def room(request, pk):  
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    return render(request, 'room.html', {'room': room})
