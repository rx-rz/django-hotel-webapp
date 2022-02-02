from datetime import datetime


class CreateBooking:
    room_ids: str
    customer_phone_number = str
    customer_email = str
    payment_type: str
    payment_id: str
    room_type: str
    booking_reference: str
    check_in: datetime
    check_out: datetime
    number_of_rooms: int
    payment_status: int
    payment_status: str
    booking_amount: float
    booking_status: str


class ListBookings:
    payment_type: int
    customer_phone_number = str
    customer_email = str
    payment_id: str
    booking_reference: int
    booking_amount: float
    check_in: datetime
    check_out: datetime
    number_of_rooms: int
    room_ids: str
    room_type: str
    name: str
    booking_status: str


class BookingDetails:
    room_ids: str
    booking_reference: int
    check_in: datetime
    check_out: datetime
    room_number: int
    room_type: str
    payment_status: int
    customer_phone_number = str
    customer_email = str


class BookingAmount:
    booking_reference: str
    booking_amount: float


class ChangeCheckOut:
    booking_reference: str
    check_out: datetime


class ChangeRoomType:
    booking_reference: str
    room_type: str


class ChangePaymentStatus:
    booking_reference: str
    payment_status: str


class ChangeBookingStatus:
    booking_reference: str
    booking_status: str


class BookingID:
    booking_reference: str


class BookedRoomID:
    room_ids: int

class BookingTerm:
    term: str