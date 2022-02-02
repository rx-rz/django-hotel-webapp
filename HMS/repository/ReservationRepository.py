from abc import abstractmethod, ABCMeta
from typing import List

from HMS.models import Reservation
from HMS.dto.ReservationDto import *


class ReservationRepository(metaclass=ABCMeta):
    def create_reservation(self, model: CreateReservation):
        """create a reservation object"""
        raise NotImplemented

    def list_reservation(self) -> List[ListReservations]:
        """list all reservation objects"""
        raise NotImplemented

    def list_reservations_by_a_particular_term(self, term) -> List[ListReservations]:
        """list all reservation objects"""
        raise NotImplemented

    def get_reservation_by_booking_reference(self, model: ReservationDetails):
        """gets reservation object by the booking reference"""
        raise NotImplemented

    def change_check_out_date(self, model: ChangeCheckOut):
        """changes the check out date for the reservation object"""
        raise NotImplemented


class DjangoORMAReservationRepository(ReservationRepository):
    def create_reservation(self, model: CreateReservation):
        reservation = Reservation()
        reservation.booking_reference = model.booking_reference
        reservation.room_number = model.room_number
        reservation.guest_name = model.guest_name
        reservation.check_in = model.check_in
        reservation.check_out = model.check_out
        reservation.save()

    def list_reservation(self) -> List[ListReservations]:
        reservations: list = Reservation.objects.values('booking_reference', 'room_number', 'guest_name', 'check_in',
                                                        'check_out')
        result: List[ListReservations] = []
        item = ListReservations()
        for reservation in reservations:
            item.room_number = reservation['room_number']
            item.booking_reference = reservation['booking_reference']
            item.guest_name = reservation['guest_name']
            item.check_in = reservation['check_in']
            item.check_out = reservation['check_out']
            result.append(item)
        return result

    def list_reservations_by_a_particular_term(self, term) -> List[ListReservations]:
        reservations: list = Reservation.objects.filter('booking_reference', 'room_number', 'guest_name', 'check_in',
                                                        'check_out').order_by(term)
        result: List[ListReservations] = []
        item = ListReservations()
        for reservation in reservations:
            item.room_number = reservation['room_number']
            item.booking_reference = reservation['booking_reference']
            item.guest_name = reservation['guest_name']
            item.check_in = reservation['check_in']
            item.check_out = reservation['check_out']
            result.append(item)
        return result

    def get_reservation_by_booking_reference(self, model: ReservationDetails):
        reservation = Reservation.objects.get(booking_reference=model.booking_reference)
        item = ReservationDetails()
        item.booking_reference = reservation.booking_reference
        item.room_number = reservation.room_number
        item.check_in = reservation.check_in
        item.check_out = reservation.check_out
        item.guest_name = reservation.guest_name
        return item

    def change_check_out_date(self, model: ChangeCheckOut):
        reservation = Reservation.objects.get(booking_reference=model.booking_reference)
        reservation.check_out = model.check_out
        reservation.save()
