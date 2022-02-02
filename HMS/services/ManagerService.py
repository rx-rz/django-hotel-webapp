from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User, Group

from HMS.repository.ManagerRepository import ManagerRepository
from HMS.dto.ManagerDto import *


class ManagerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_manager(self, model: RegisterManager) -> int:
        """returns a manager object"""
        raise NotImplemented

    @abstractmethod
    def edit_manager(self, manager_id: int, model: EditManager):
        """edits the manager object"""
        raise NotImplemented

    @abstractmethod
    def manager_details(self, manager_id: int) -> List[ManagerDetails]:
        """shows maanager details"""
        raise NotImplemented

    @abstractmethod
    def get_manager_details_by_password(self, password: str) -> ManagerDetails:
        """get the details of manager object by its password"""
        raise NotImplemented

    @abstractmethod
    def get_manager_details_by_email(self, email: str) -> ManagerDetails:
        """get the details of the manager object by its email"""
        raise NotImplemented


class DefaultManagerManagementService(ManagerManagementService):
    repository: ManagerRepository

    def __init__(self, repository: ManagerRepository):
        self.repository = repository

    def create_manager(self, model: RegisterManager) -> int:
        return self.create_manager(model)

    def edit_manager(self, manager_id: int, model: EditManager):
        return self.edit_manager(manager_id, model)

    def get_manager_details_by_password(self, password: str) -> ManagerDetails:
        return self.get_manager_details_by_password(password)

    def get_manager_details_by_email(self, email: str) -> ManagerDetails:
        return self.get_manager_details_by_email(email)

    def manager_details(self, manager_id: int) -> List[ManagerDetails]:
        return self.repository.manager_details(manager_id)
