from abc import ABCMeta, abstractmethod

from django.contrib.auth.models import User, Group

from HMS.models import Customer
from HMS.dto.CustomerDto import *
from typing import List

from HMS.repository.CustomerRepository import CustomerRepository


class CustomerManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_customer(self, model: RegisterCustomer) -> int:
        """creates a customer object"""
        raise NotImplemented

    @abstractmethod
    def edit_customer(self, customer_id: int, model: CustomerDetails):
        """edits the customer object"""
        raise NotImplemented

    @abstractmethod
    def customer_details(self, customer_id: int) -> List[CustomerDetails]:
        """shows the customer details"""
        raise NotImplemented

    @abstractmethod
    def list_customers(self) -> List[ListCustomers]:
        """lists all the customer objects"""
        raise NotImplemented

    @abstractmethod
    def list_customers_by_a_particular_term(self, term) -> List[ListCustomers]:
        """lists all the customer objects"""
        raise NotImplemented

    @abstractmethod
    def get_customer_by_email(self, model: CustomerDetails, email: str):
        """get customer details by email or their password"""
        raise NotImplemented

    @abstractmethod
    def get_customer_by_password(self, model: CustomerDetails, password: str):
        raise NotImplemented

    @abstractmethod
    def get_customer_by_id(self, model: CustomerDetails, user_id: int):
        raise NotImplemented


class DefaultCustomerManagementService(CustomerManagementService):
    repository: CustomerRepository

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def create_customer(self, model: RegisterCustomer) -> int:
        return self.repository.create_customer(model)

    def edit_customer(self, customer_id: int, model: CustomerDetails):
        return self.repository.edit_customer(customer_id, model)

    def customer_details(self, customer_id: int) -> List[CustomerDetails]:
        return self.repository.customer_details(customer_id)

    def list_customers(self) -> List[ListCustomers]:
        return self.repository.list_customers()

    def list_customers_by_a_particular_term(self, term) -> List[ListCustomers]:
        return self.repository.list_customers_by_a_particular_term(term)

    def get_customer_by_password(self, model: CustomerDetails, password: str):
        return self.repository.get_customer_by_password(model, password)

    def get_customer_by_email(self, model: CustomerDetails, email: str):
        return self.repository.get_customer_by_email(model, email)

    def get_customer_by_id(self, model: CustomerDetails, user_id: int):
        return self.repository.get_customer_by_id(model, user_id)
