from abc import ABCMeta, abstractmethod

from django.contrib.auth.models import User, Group

from HMS.models import Customer
from HMS.dto.CustomerDto import *
from typing import List, Type


class CustomerRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_customer(self, model: RegisterCustomer) -> int:
        """creates a customer object"""
        raise NotImplemented

    @abstractmethod
    def edit_customer(self, user_id: int, model: CustomerDetails):
        """edits the customer object"""
        raise NotImplemented

    @abstractmethod
    def customer_details(self, user_id: int) -> List[CustomerDetails]:
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


class DjangoORMACustomerRepository(CustomerRepository):
    def create_customer(self, model: RegisterCustomer) -> Type[int]:
        customer = Customer()
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.username = model.username

        customer.user = user
        group = Group.objects.get(name="Customers")
        user.groups.add(group)

        user.save()
        customer.date_of_birth = model.date_of_birth
        customer_id = customer.user_id
        customer.phone_number = model.phone_number

        customer.save()
        return customer_id

    def edit_customer(self, customer_id: int, model: CustomerDetails):
        customer = Customer.objects.get(user_id=customer_id)
        customer.user.first_name = model.first_name
        customer.user.last_name = model.last_name
        customer.phone_number = model.phone_number
        customer.date_of_birth = model.date_of_birth
        customer.save()

    def customer_details(self, customer_id: int):
        customer = Customer.objects.values('user__first_name', 'user__last_name',
                                           'user__email', 'phone_number', 'date_of_birth',
                                           'user__username').get(user_id=customer_id)

        item = CustomerDetails()
        try:
            item.first_name = customer['user__first_name']
            item.last_name = customer['user__last_name']
            item.email = customer['user__email']
            item.phone_number = customer['phone_number']
            item.date_of_birth = customer['date_of_birth']
            item.username = customer['user__username']
            return item
        except Customer.DoesNotExist as e:
            raise e

    def list_customers(self) -> List[ListCustomers]:
        customers = list(Customer.objects.values('user__first_name', 'user__last_name', 'user__email', 'phone_number',
                                                 'date_of_birth'))
        results: List[ListCustomers] = []
        for customer in customers:
            item = ListCustomers()
            item.first_name = customer['user__first_name']
            item.last_name = customer['user__last_name']
            item.email = customer['user__email']
            item.phone_number = customer['phone_number']
            item.date_of_birth = customer['date_of_birth']
            results.append(item)
        return results

    def list_customers_by_a_particular_term(self, term) -> List[ListCustomers]:
        customers = list(Customer.objects.filter('user__first_name', 'user__last_name', 'user__email', 'phone_number',
                                                 'date_of_birth', 'address').order_by(term))
        result: List[ListCustomers] = []
        for customer in customers:
            item = ListCustomers()
            item.first_name = customer['user__first_name']
            item.last_name = customer['user__last_name']
            item.email = customer['user__email']
            item.phone_number = customer['phone_number']
            item.date_of_birth = customer['date_of_birth']
            result.append(item)
        return result

    def get_customer_by_email(self, model: CustomerDetails, email: str):
        customer = Customer.objects.get(email=email).values('user_id', 'user__first_name', 'user__last_name',
                                                            'user__email',
                                                            'phone_number', 'date_of_birth')
        item = CustomerDetails()
        item.id = customer['user_id']
        item.first_name = customer['user__first_name']
        item.last_name = customer['user__last_name']
        item.email = customer['user__email']
        item.phone_number = customer['phone_number']
        item.date_of_birth = customer['date_of_birth']
        return item

    def get_customer_by_password(self, model: CustomerDetails, password: str):
        customer = Customer.objects.get(password=password).values('user_id', 'user__first_name', 'user__last_name',
                                                                  'user__email',
                                                                  'phone_number', 'date_of_birth')
        item = CustomerDetails()
        item.id = customer['user_id']
        item.first_name = customer['user__first_name']
        item.last_name = customer['user__last_name']
        item.email = customer['user__email']
        item.phone_number = customer['phone_number']
        item.date_of_birth = customer['date_of_birth']
        return item

    def get_customer_by_id(self, model: CustomerDetails, user_id: int):
        customer = Customer.objects.filter(user_id=user_id).values('user__username', 'user__first_name',
                                                                   'user__last_name', 'user__email', 'phone_number',
                                                                   'date_of_birth')
        item = CustomerDetails()
        item.id = customer['user_id']
        item.first_name = customer['user__first_name']
        item.last_name = customer['user__last_name']
        item.email = customer['user__email']
        item.phone_number = customer['phone_number']
        item.date_of_birth = customer['date_of_birth']
        return item
