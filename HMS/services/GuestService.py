from abc import abstractmethod, ABCMeta
from typing import List

from HMS.models import Guest
from HMS.dto.GuestDto import *
from HMS.repository.GuestRepository import GuestRepository


class GuestManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_guest(self, model: CreateGuest):
        raise NotImplementedError

    @abstractmethod
    def change_guest_status(self, model: ChangeStatus):
        raise NotImplementedError

    @abstractmethod
    def list_guests(self) -> List[ListGuests]:
        raise NotImplementedError

    @abstractmethod
    def list_guests_by_a_particular_term(self, term) -> List[ListGuests]:
        raise NotImplementedError

    @abstractmethod
    def change_check_out(self, model: ChangeCheckOut):
        raise NotImplementedError

    @abstractmethod
    def change_guest_balance(self, model: ChangeBalance):
        raise NotImplementedError


class DefaultGuestManagementService(GuestManagementService):
    repository: GuestRepository

    def __init__(self, repository: GuestRepository):
        self.repository = repository

    def create_guest(self, model: CreateGuest):
        return self.repository.create_guest(model)

    def change_guest_status(self, model: ChangeStatus):
        return self.repository.change_guest_status(model)

    def change_guest_balance(self, model: ChangeBalance):
        return self.repository.change_guest_balance(model)

    def change_check_out(self, model: ChangeCheckOut):
        return self.repository.change_check_out(model)

    def list_guests(self) -> List[ListGuests]:
        return self.repository.list_guests()

    def list_guests_by_a_particular_term(self, term) -> List[ListGuests]:
        return self.repository.list_guests_by_a_particular_term(term)
