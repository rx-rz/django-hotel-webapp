from django.urls import path
from HMS.views.Rooms import room_view

urlpatterns = [
    path('register', room_view.create_room, name='create_room'),
    path('list_rooms', room_view.list_rooms, name='list_rooms')

]
