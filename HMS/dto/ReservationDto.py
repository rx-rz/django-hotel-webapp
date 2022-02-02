from datetime import datetime


class CreateReservation:
    booking_reference: str
    guest_name: str
    room_number: str
    check_in: datetime
    check_out: datetime


class ListReservations:
    booking_reference: str
    guest_name: str
    room_number: str
    check_in: datetime
    check_out: datetime


class ReservationDetails:
    booking_reference: str
    guest_name: str
    room_number: str
    check_in: datetime
    check_out: datetime


class ChangeCheckOut:
    booking_reference: str
    check_out: str
