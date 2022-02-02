from abc import abstractmethod, ABCMeta
from typing import List
from HMS.repository.BookingRepository import BookingRepository
from HMS.dto.BookingDto import *


class BookingManagementService(metaclass=ABCMeta):
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
    def get_booking_by_booking_reference(self, booking_reference: str):
        """get booking details by the booking reference"""
        raise NotImplemented

    @abstractmethod
    def change_booking_status(self, model: ChangeBookingStatus):
        """change booking status"""
        raise NotImplemented


class DefaultBookingManagementService(BookingManagementService):
    repository: BookingRepository

    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def create_booking(self, model: CreateBooking):
        return self.repository.create_booking(model)

    def list_bookings(self) -> List[ListBookings]:
        return self.repository.list_bookings()

    def change_booking_amount(self, model: BookingAmount):
        return self.repository.change_booking_amount(model)

    def change_check_out_date(self, model: ChangeCheckOut):
        return self.repository.change_check_out_date(model)

    def change_room_type(self, model: ChangeRoomType):
        return self.repository.change_room_type(model)

    def change_booking_payment_status(self, model: ChangePaymentStatus):
        return self.repository.change_booking_payment_status(model)

    def get_booking_by_booking_reference(self, booking_reference: str):
        return self.repository.get_booking_by_booking_reference(booking_reference)

    def list_active_bookings(self) -> List[ListBookings]:
        return self.repository.list_active_bookings()

    def list_inactive_bookings(self) -> List[ListBookings]:
        return self.repository.list_inactive_bookings()

    def change_booking_status(self, model: ChangeBookingStatus):
        return self.repository.change_booking_status(model)