from abc import abstractmethod, ABCMeta
from typing import List
from HMS.models import Rooms
from HMS.dto.RoomDto import *


class RoomRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_room(self, model: CreateRoom):
        raise NotImplementedError

    @abstractmethod
    def list_rooms(self) -> List[ListRooms]:
        raise NotImplementedError

    @abstractmethod
    def list_rooms_by_a_particular_term(self, term) -> List[ListRooms]:
        raise NotImplementedError

    @abstractmethod
    def change_room_status(self, model: ChangeRoomStatus):
        raise NotImplementedError

    @abstractmethod
    def change_room_type(self, model: ChangeRoomType):
        raise NotImplementedError

    @abstractmethod
    def get_room_by_room_number(self, room_number: int) -> RoomDetails:
        raise NotImplementedError


class DjangoORMARoomRepository(RoomRepository):
    def create_room(self, model: CreateRoom):
        room = Rooms()
        room.room_id = model.room_id
        room.room_type = model.room_type
        room.room_number = model.room_number
        room.room_status = model.room_status
        room.save()

    def list_rooms(self) -> List[ListRooms]:
        rooms = list(Rooms.objects.values('room_id', 'room_type', 'room_status', 'room_number'))
        results: List[ListRooms] = []
        for room in rooms:
            item = ListRooms()
            item.room_id = room['room_id']
            item.room_type = room['room_type']
            item.room_status = room['room_status']
            item.room_number = room['room_number']
            results.append(item)
        return results

    def list_rooms_by_a_particular_term(self, term) -> List[ListRooms]:
        rooms = list(Rooms.objects.values('room_id', 'room_type', 'room_status', 'room_number'))
        results: List[ListRooms] = []
        for room in rooms:
            item = ListRooms()
            item.room_id = room['room_id']
            item.room_type = room['room_type']
            item.room_status = room['room_status']
            item.room_number = room['room_number']
            results.append(item)
        return results

    def change_room_type(self, model: ChangeRoomType):
        room = Rooms.objects.get(room_number=model.room_number)
        room.room_type = model.room_type
        room.save()

    def get_room_by_room_number(self, room_number: int) -> RoomDetails:
        item = RoomDetails()
        room = Rooms.objects.get(room_number=room_number)
        item.room_id = room.room_id
        item.room_number = room.room_number
        item.room_type = room.room_type
        item.room_status = room.room_status
        return item

    def change_room_status(self, model: ChangeRoomStatus):
        room = Rooms.objects.get(room_number=model.room_number)
        room.room_status = model.room_status
        room.save()
