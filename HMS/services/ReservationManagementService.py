from abc import abstractmethod, ABCMeta
from typing import List

from HMS.models import Reservation
from HMS.dto.ReservationDto import *
from HMS.repository.ReservationRepository import ReservationRepository


class ReservationManagementService(metaclass=ABCMeta):
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


class DefaultReservationManagementService(ReservationManagementService):
    repository: ReservationRepository

    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    def create_reservation(self, model: CreateReservation):
        return self.repository.create_reservation(model)

    def list_reservation(self) -> List[ListReservations]:
        return self.repository.list_reservation()

    def list_reservations_by_a_particular_term(self, term) -> List[ListReservations]:
        return self.repository.list_reservations_by_a_particular_term(term)

    def get_reservation_by_booking_reference(self, model: ReservationDetails):
        return self.repository.get_reservation_by_booking_reference(model)

    def change_check_out_date(self, model: ChangeCheckOut):
        return self.repository.change_check_out_date(model)
