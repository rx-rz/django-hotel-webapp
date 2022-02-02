from datetime import datetime


class CreatePayment:
    customer_name: str
    booking_reference: str
    payment_status: str
    payment_type: str
    amount: float
    balance: float
    date_of_payment: datetime


class ChangePaymentStatus:
    booking_reference: str
    payment_status: str


class DepositPayment:
    booking_reference: str
    amount: float
    balance: float

