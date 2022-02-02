from django.db import models
from django.contrib.auth.models import User
import datetime


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    phone_number = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"""{self.user.first_name}\t{self.user.last_name}\t{self.phone_number}"""


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    phone_number = models.CharField(max_length=14)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)

    def __str__(self):
        return f"""{self.user.first_name}\t{self.user.last_name}\t{self.phone_number}"""


class Rooms(models.Model):
    room_id = models.IntegerField()
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=20)
    room_status = models.CharField(max_length=20)

    def __str__(self):
        return f"""{self.room_number}\t{self.room_status}\t{self.room_type}"""


class Booking(models.Model):
    payment_id = models.CharField(null=True, max_length=40)
    payment_type = models.CharField(max_length=40, null=True)
    payment_status = models.CharField(max_length=40, null=True)
    email = models.CharField(max_length=70, null=True)
    room_ids = models.CharField(max_length=200, null=True)
    customer_phone_number = models.CharField(max_length=50, default=True, null=True)
    customer_email = models.CharField(max_length=50, default=True, null=True)
    room_type = models.CharField(max_length=40, null=True)
    booking_reference = models.CharField(max_length=50, null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    number_of_rooms = models.IntegerField()
    booking_amount = models.FloatField(null=True)
    booking_status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"""{self.check_in}\t{self.check_out}\t\t{self.number_of_rooms}"""


class Payment(models.Model):
    customer_name = models.CharField(max_length=100, null=True)
    booking_reference = models.CharField(max_length=100, null=True)
    payment_status = models.CharField(max_length=20, null=True)
    payment_type = models.CharField(max_length=40, null=True)
    amount = models.IntegerField()
    balance = models.IntegerField()
    date_of_payment = models.DateTimeField()

    def __str__(self):
        return f"""{self.payment_status}\t{self.amount}\t{self.balance}"""


class Guest(models.Model):
    name = models.CharField(max_length=30)
    booking_reference = models.CharField(max_length=100, null=True)
    room_numbers = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20)
    balance = models.IntegerField(null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"""{self.name}\t{self.status}"""


class Reservation(models.Model):
    booking_reference = models.CharField(max_length=100, null=True)
    guest_name = models.CharField(max_length=100, null=True)
    room_number = models.IntegerField()
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"""{self.booking_reference}\t{self.room_number}\t{self.guest_name}"""
