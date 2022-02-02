from abc import abstractmethod, ABCMeta
from HMS.models import Payment
from HMS.dto.PaymentDto import *


class PaymentRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self, model: CreatePayment):
        raise NotImplementedError

    @abstractmethod
    def make_payment(self, model: DepositPayment):
        raise NotImplementedError

    @abstractmethod
    def change_payment_status(self, model: ChangePaymentStatus):
        raise NotImplementedError


class DjangoORMAPaymentRepository(PaymentRepository):
    def create_payment(self, model: CreatePayment):
        payment = Payment()
        payment.payment_status = model.payment_status
        payment.payment_type = model.payment_type
        payment.date_of_payment = model.date_of_payment
        payment.balance = model.balance
        payment.amount = model.amount
        payment.booking_reference = model.booking_reference
        payment.customer_name = model.customer_name
        payment.save()

    def make_payment(self, model: DepositPayment):
        payment = Payment.objects.get(booking_reference=model.booking_reference)
        payment.balance = model.balance
        payment.save()

    def change_payment_status(self, model: ChangePaymentStatus):
        payment = Payment.objects.get(booking_reference=model.booking_reference)
        payment.payment_status = model.payment_status
        payment.save()
