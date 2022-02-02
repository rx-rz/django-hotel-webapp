from abc import abstractmethod, ABCMeta
from typing import List

from HMS.models import Guest
from HMS.dto.GuestDto import *


class GuestRepository(metaclass=ABCMeta):
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


class DjangoORMAGuestRepository(GuestRepository):
    def create_guest(self, model: CreateGuest):
        guest = Guest()
        guest.name = model.name
        guest.check_in = model.check_in
        guest.check_out = model.check_out
        guest.booking_reference = model.booking_reference
        guest.room_numbers = model.room_numbers
        guest.balance = model.balance
        guest.status = model.status
        guest.save()

    def change_guest_status(self, model: ChangeStatus):
        guest = Guest.objects.get(booking_reference=model.booking_reference)
        guest.status = model.status
        guest.save()

    def change_check_out(self, model: ChangeCheckOut):
        guest = Guest.objects.get(booking_reference=model.booking_reference)
        guest.check_out = model.check_out
        guest.save()

    def change_guest_balance(self, model: ChangeBalance):
        guest = Guest.objects.get(booking_reference=model.booking_reference)
        guest.balance = model.balance
        guest.save()

    def list_guests_by_a_particular_term(self, term) -> List[ListGuests]:
        guests: list = Guest.objects.filter('name', 'check_out', 'check_in', 'booking_reference', 'room_numbers',
                                            'balance', 'status').order_by(term)
        result: List[ListGuests] = []
        item = ListGuests()
        for guest in guests:
            item.name = guest['name']
            item.check_out = guest['check_out']
            item.check_in = guest['check_in']
            item.booking_reference = guest['booking_reference']
            item.room_numbers = guest['room_numbers']
            item.balance = guest['balance']
            item.status = guest['status']
            result.append(item)
        return result

    def list_guests(self) -> List[ListGuests]:
        guests: list = Guest.objects.values('name', 'check_out', 'check_in', 'booking_reference', 'room_numbers',
                                            'balance', 'status')
        result: List[ListGuests] = []
        item = ListGuests()
        for guest in guests:
            item.name = guest['name']
            item.check_out = guest['check_out']
            item.check_in = guest['check_in']
            item.booking_reference = guest['booking_reference']
            item.room_numbers = guest['room_numbers']
            item.balance = guest['balance']
            item.status = guest['status']
            result.append(item)
        return result
