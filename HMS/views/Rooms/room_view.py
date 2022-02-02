from django.http import HttpRequest
from django.shortcuts import redirect, render

from HMS.dto.RoomDto import CreateRoom
from HMS.service_provider import hotel_service_provider


def __get_attribute_from_request(request: HttpRequest):
    create_room_dto = CreateRoom()
    create_room_dto.room_type = request.POST['type_of_room']
    return create_room_dto


def __get_attribute_from_request_for_number_of_rooms(request: HttpRequest):
    number_of_rooms = request.POST['number_of_rooms']
    return int(number_of_rooms)


def __create_room_if_post_method(request, context):
    if request.method == 'POST':
        count = 0
        number_of_rooms = __get_attribute_from_request_for_number_of_rooms(request)
        room = __get_attribute_from_request(request)
        while count < number_of_rooms:
            if room:
                room.room_number = __room_number()
                room.room_status = 'inactive'
                room.room_id = room.room_number
                hotel_service_provider.room_management_service().create_room(room)
                context['saved'] = True
                count += 1
            else:
                context['saved'] = False


def list_rooms(request):
    rooms = hotel_service_provider.room_management_service().list_rooms()
    context = {
        'rooms': rooms
    }

    return render(request, 'rooms/list_rooms.html', context)


def create_room(request):
    context = {

    }
    __create_room_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('home')
    return render(request, 'rooms/create_room.html', context)


def __room_number():
    try:
        rooms: list = hotel_service_provider.room_management_service().list_rooms()
        if rooms:
            room_number = len(rooms) + 1
            return room_number
        else:
            return 1
    except TypeError:
        room_number = 1
        return room_number
