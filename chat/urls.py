# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('profile/', views.profile_view, name='profile'),
    path('rooms/', views.room_choice_view, name='room_choice'),
]
