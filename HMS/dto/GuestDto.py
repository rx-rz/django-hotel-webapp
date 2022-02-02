from datetime import datetime


class CreateGuest:
    name: str
    booking_reference: str
    room_numbers: int
    status: str
    balance: float
    check_in: datetime
    check_out: datetime


class ListGuests:
    name: str
    booking_reference: str
    room_numbers: int
    status: str
    balance: float
    check_in: datetime
    check_out: datetime


class ChangeBalance:
    booking_reference: str
    balance: float


class ChangeStatus:
    booking_reference: str
    status: float


class ChangeCheckOut:
    booking_reference: str
    check_out: datetime
