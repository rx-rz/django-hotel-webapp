from abc import abstractmethod, ABCMeta
from typing import List
from HMS.models import Rooms
from HMS.dto.RoomDto import *
from HMS.repository.RoomRepository import RoomRepository


class RoomManagementService(metaclass=ABCMeta):
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


class DefaultRoomManagementService(RoomManagementService):
    repository = RoomRepository

    def __init__(self, repository: RoomRepository):
        self.repository = repository

    def create_room(self, model: CreateRoom):
        return self.repository.create_room(model)

    def list_rooms(self) -> List[ListRooms]:
        return self.repository.list_rooms()

    def list_rooms_by_a_particular_term(self, term) -> List[ListRooms]:
        return self.repository.list_rooms_by_a_particular_term(term)

    def change_room_status(self, model: ChangeRoomStatus):
        return self.repository.change_room_status(model)

    def change_room_type(self, model: ChangeRoomType):
        return self.repository.change_room_type(model)

    def get_room_by_room_number(self, room_number: int) -> RoomDetails:
        return self.repository.get_room_by_room_number(room_number)
