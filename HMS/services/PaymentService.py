from abc import abstractmethod, ABCMeta
from HMS.models import Payment
from HMS.dto.PaymentDto import *
from HMS.repository.PaymentRepository import PaymentRepository


class PaymentManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self, model: CreatePayment):
        raise NotImplementedError

    @abstractmethod
    def make_payment(self, model: DepositPayment):
        raise NotImplementedError

    @abstractmethod
    def change_payment_status(self, model: ChangePaymentStatus):
        raise NotImplementedError


class DefaultPaymentManagementService(PaymentManagementService):
    repository: PaymentRepository

    def __init(self, repository: PaymentRepository):
        self.repository = repository

    def create_payment(self, model: CreatePayment):
        return self.repository.create_payment(model)

    def make_payment(self, model: DepositPayment):
        return self.repository.make_payment(model)

    def change_payment_status(self, model: ChangePaymentStatus):
        return self.repository.change_payment_status(model)
