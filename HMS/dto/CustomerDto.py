from datetime import datetime


class RegisterCustomer:
    id: int
    first_name: str
    last_name: str
    phone_number: str
    username: str
    email: str
    password: str
    confirm_password: str
    date_of_birth: datetime


class CustomerDetails:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    address: str
    phone_number: str
    date_of_birth: datetime


class ListCustomers:
    id: int
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    date_of_birth: datetime


class CustomerID:
    id: int


class CustomerFirstName:
    first_name: str
