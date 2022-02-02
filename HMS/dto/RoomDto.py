class CreateRoom:
    room_id: int
    room_number: int
    room_type: str
    room_status: str


class ListRooms:
    room_id: int
    room_number: int
    room_type: str
    room_status: str


class ChangeRoomStatus:
    room_number: int
    room_status: str


class ChangeRoomType:
    room_number: int
    room_type: str


class RoomDetails:
    room_id: int
    room_number: int
    room_type: str
    room_status: str
