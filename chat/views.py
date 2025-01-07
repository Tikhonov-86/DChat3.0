# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})


def profile_view(request):
    return render(request, 'chat/profile.html')


def room_choice_view(request):
    return render(request, 'chat/room_choice.html')
