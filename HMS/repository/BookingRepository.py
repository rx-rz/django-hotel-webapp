from abc import abstractmethod, ABCMeta
from typing import List

from HMS.models import Booking
from HMS.dto.BookingDto import *


class BookingRepository(metaclass=ABCMeta):

    @abstractmethod
    def create_booking(self, model: CreateBooking):
        """creates booking object"""
        raise NotImplemented

    @abstractmethod
    def list_bookings(self) -> List[ListBookings]:
        """lists booking object instances"""
        raise NotImplemented

    @abstractmethod
    def list_active_bookings(self) -> List[ListBookings]:
        """list active booking object instances"""
        raise NotImplemented

    @abstractmethod
    def list_inactive_bookings(self) -> List[ListBookings]:
        """list inactive booking object instances"""
        raise NotImplemented

    @abstractmethod
    def get_booking_by_booking_reference(self, booking_reference: str):
        """get booking details by the booking reference"""
        raise NotImplemented

    @abstractmethod
    def change_booking_amount(self, model: BookingAmount):
        """edit booking amount"""
        raise NotImplemented

    @abstractmethod
    def change_check_out_date(self, model: ChangeCheckOut):
        """change check out date"""
        raise NotImplemented

    @abstractmethod
    def change_room_type(self, model: ChangeRoomType):
        """change booking room type"""
        raise NotImplemented

    @abstractmethod
    def change_booking_payment_status(self, model: ChangePaymentStatus):
        """change booking payment status"""
        raise NotImplemented

    @abstractmethod
    def change_booking_status(self, model: ChangeBookingStatus):
        """change booking status"""
        raise NotImplemented


class DjangoORMABookingRepository(BookingRepository):
    def create_booking(self, model: CreateBooking):
        booking = Booking()
        booking.booking_reference = model.booking_reference
        booking.booking_amount = model.booking_amount
        booking.room_type = model.room_type
        booking.customer_email = model.customer_email
        booking.customer_phone_number = model.customer_phone_number
        booking.check_in = model.check_in
        booking.check_out = model.check_out
        booking.number_of_rooms = model.number_of_rooms
        booking.payment_id = model.payment_id
        booking.payment_status = model.payment_status
        booking.payment_type = model.payment_type
        booking.booking_status = model.booking_status
        booking.room_ids = model.room_ids
        booking.save()

    def list_bookings(self) -> List[ListBookings]:
        bookings: list = Booking.objects.values('booking_reference', 'booking_amount', 'room_type',
                                                'customer_email', 'customer_phone_number', 'check_in', 'check_out',
                                                'number_of_rooms', 'payment_id', 'payment_status', 'payment_type',
                                                'room_ids', 'booking_status')
        result: list = []
        item = ListBookings()
        for booking in bookings:
            item.booking_reference = booking['booking_reference']
            item.booking_amount = booking['booking_amount']
            item.room_type = booking['room_type']
            item.customer_email = booking['customer_email']
            item.customer_phone_number = booking['customer_phone_number']
            item.check_in = booking['check_in']
            item.check_out = booking['check_out']
            item.number_of_rooms = booking['number_of_rooms']
            item.payment_id = booking['payment_id']
            item.payment_status = booking['payment_status']
            item.payment_type = booking['payment_type']
            item.room_ids = booking['room_ids']
            item.booking_status = booking['booking_status']
            result.append(item)
        return result

    def list_active_bookings(self) -> List[ListBookings]:
        bookings: list = Booking.objects.filter(booking_status='active').values('booking_reference', 'booking_amount',
                                                                                'room_type',
                                                                                'customer_email',
                                                                                'customer_phone_number', 'check_in',
                                                                                'check_out',
                                                                                'number_of_rooms', 'payment_id',
                                                                                'payment_status', 'payment_type',
                                                                                'room_ids', 'booking_status')
        result: list = []
        item = ListBookings()
        for booking in bookings:
            item.booking_reference = booking['booking_reference']
            item.booking_amount = booking['booking_amount']
            item.room_type = booking['room_type']
            item.customer_email = booking['customer_email']
            item.customer_phone_number = booking['customer_phone_number']
            item.check_in = booking['check_in']
            item.check_out = booking['check_out']
            item.number_of_rooms = booking['number_of_rooms']
            item.payment_id = booking['payment_id']
            item.payment_status = booking['payment_status']
            item.payment_type = booking['payment_type']
            item.room_ids = booking['room_ids']
            item.booking_status = booking['booking_status']
            result.append(item)
        return result

    def list_inactive_bookings(self) -> List[ListBookings]:
        bookings: list = Booking.objects.filter(booking_status='inactive').values('booking_reference', 'booking_amount',
                                                                                  'room_type',
                                                                                  'customer_email',
                                                                                  'customer_phone_number', 'check_in',
                                                                                  'check_out',
                                                                                  'number_of_rooms', 'payment_id',
                                                                                  'payment_status', 'payment_type',
                                                                                  'room_ids', 'booking_status')
        result: list = []
        item = ListBookings()
        for booking in bookings:
            item.booking_reference = booking['booking_reference']
            item.booking_amount = booking['booking_amount']
            item.room_type = booking['room_type']
            item.customer_email = booking['customer_email']
            item.customer_phone_number = booking['customer_phone_number']
            item.check_in = booking['check_in']
            item.check_out = booking['check_out']
            item.number_of_rooms = booking['number_of_rooms']
            item.payment_id = booking['payment_id']
            item.payment_status = booking['payment_status']
            item.payment_type = booking['payment_type']
            item.room_ids = booking['room_ids']
            item.booking_status = booking['booking_status']
            result.append(item)
        return result

    def get_booking_by_booking_reference(self, booking_reference: str):
        item = BookingDetails()
        booking = Booking.objects.get(booking_reference=booking_reference)
        item.booking_reference = booking.booking_reference
        item.room_number = booking.number_of_rooms

        item.room_type = booking.room_type
        item.check_in = booking.check_in
        item.check_out = booking.check_out
        item.customer_phone_number = booking.customer_phone_number
        item.customer_email = booking.customer_email
        item.payment_status = booking.payment_status
        item.room_ids = booking.room_ids
        return item

    def change_booking_amount(self, model: BookingAmount):
        booking = Booking.objects.get(booking_reference=model.booking_reference)
        booking.booking_amount = model.booking_amount
        booking.save()

    def change_booking_status(self, model: ChangeBookingStatus):
        booking = Booking.objects.get(booking_reference=model.booking_reference)
        booking.booking_status = model.booking_status
        booking.save()

    def change_room_type(self, model: ChangeRoomType):
        booking = Booking.objects.get(booking_reference=model.booking_reference)
        booking.room_type = model.room_type
        booking.save()

    def change_booking_payment_status(self, model: ChangePaymentStatus):
        booking = Booking.objects.get(booking_reference=model.booking_reference)
        booking.payment_status = model.payment_status
        booking.save()

    def change_check_out_date(self, model: ChangeCheckOut):
        booking = Booking.objects.get(booking_reference=model.booking_reference)
        booking.check_out = model.check_out
        booking.save()
