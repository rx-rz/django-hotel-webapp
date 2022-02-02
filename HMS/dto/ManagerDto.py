from datetime import datetime


class RegisterManager:
    manager_id: int
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    confirm_password: str
    address: str
    phone_number: str
    date_of_birth: datetime


class ManagerDetails:
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    address: str
    phone_number: str
    date_of_birth: datetime


class EditManager:
    manager_id: int
    first_name: str
    last_name: str
    username: str
    email: str
    address: str
    phone_number: str
    date_of_birth: datetime
