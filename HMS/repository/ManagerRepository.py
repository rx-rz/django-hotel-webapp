from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User, Group

from HMS.models import Manager
from HMS.dto.ManagerDto import *


class ManagerRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_manager(self, model: RegisterManager) -> int:
        """returns a manager object"""
        raise NotImplemented

    @abstractmethod
    def edit_manager(self, user_id: int, model: EditManager):
        """edits the manager object"""
        raise NotImplemented

    @abstractmethod
    def manager_details(self, manager_id: int) -> List[ManagerDetails]:
        """shows manager details"""
        raise NotImplemented

    @abstractmethod
    def get_manager_details_by_password(self, password: str) -> ManagerDetails:
        """get the details of manager object by its password"""
        raise NotImplemented

    @abstractmethod
    def get_manager_details_by_email(self, email: str) -> ManagerDetails:
        """get the details of the manager object by its email"""
        raise NotImplemented


class DjangoORMAManagerRepository(ManagerRepository):
    def create_manager(self, model: RegisterManager) -> int:
        manager = Manager()
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name

        manager.user = user
        group = Group.objects.get(name="Managers")
        user.groups.add(group)

        user.save()

        manager.phone_number = model.phone_number
        manager.address = model.address
        manager.date_of_birth = model.date_of_birth
        manager.save()
        manager_id = manager.id
        return manager_id

    def edit_manager(self, manager_id: int, model: EditManager):
        manager = Manager.objects.get(manager_id=manager_id)
        manager.user.first_name = model.first_name
        manager.user.last_name = model.last_name
        manager.address = model.address
        manager.phone_number = model.phone_number
        manager.date_of_birth = model.date_of_birth
        manager.save()

    def manager_details(self, manager_id: int):
        manager = Manager.objects.values('user__first_name', 'user__last_name', 'user__email', 'phone_number',
                                         'date_of_birth', 'user__username').get(user_id=manager_id)

        item = ManagerDetails()
        try:
            item.first_name = manager['user__first_name']
            item.last_name = manager['user__last_name']
            item.email = manager['user__email']
            item.phone_number = manager['phone_number']
            item.date_of_birth = manager['date_of_birth']
            item.username = manager['user__username']
            return item
        except Manager.DoesNotExist as e:
            raise e

    def get_manager_details_by_email(self, email: str) -> ManagerDetails:
        manager = Manager.objects.get(user__email=email).values('user_id', 'user__first_name', 'user__last_name',
                                                                'user__email', 'address',
                                                                'phone_number', 'date_of_birth')
        item = ManagerDetails()
        item.id = manager['user__id']
        item.first_name = manager['user__first_name']
        item.last_name = manager['user__last_name']
        item.email = manager['user__email']
        item.address = manager['address']
        item.phone_number = manager['phone_number']
        item.date_of_birth = manager['date_of_birth']
        return item

    def get_manager_details_by_password(self, password: str) -> ManagerDetails:
        manager = Manager.objects.get(user__password=password).values('user_id', 'user__first_name', 'user__last_name',
                                                                      'user__email', 'address',
                                                                      'phone_number', 'date_of_birth')
        item = ManagerDetails()
        item.id = manager['user__id']
        item.first_name = manager['user__first_name']
        item.last_name = manager['user__last_name']
        item.email = manager['user__email']
        item.address = manager['address']
        item.phone_number = manager['phone_number']
        item.date_of_birth = manager['date_of_birth']
        return item
