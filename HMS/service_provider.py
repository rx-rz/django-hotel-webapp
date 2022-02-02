from typing import Callable

from dependency_injector import containers, providers

from HMS.repository.CustomerRepository import CustomerRepository, DjangoORMACustomerRepository
from HMS.services.CustomerService import CustomerManagementService, DefaultCustomerManagementService

from HMS.repository.ManagerRepository import ManagerRepository, DjangoORMAManagerRepository
from HMS.services.ManagerService import ManagerManagementService, DefaultManagerManagementService

from HMS.repository.ReservationRepository import ReservationRepository, DjangoORMAReservationRepository
from HMS.services.ReservationManagementService import ReservationManagementService, DefaultReservationManagementService

from HMS.repository.GuestRepository import GuestRepository, DjangoORMAGuestRepository
from HMS.services.GuestService import GuestManagementService, DefaultGuestManagementService

from HMS.repository.RoomRepository import RoomRepository, DjangoORMARoomRepository
from HMS.services.RoomService import RoomManagementService, DefaultRoomManagementService

from HMS.repository.BookingRepository import BookingRepository, DjangoORMABookingRepository
from HMS.services.BookingService import BookingManagementService, DefaultBookingManagementService

from HMS.repository.PaymentRepository import PaymentRepository, DjangoORMAPaymentRepository
from HMS.services.PaymentService import PaymentManagementService, DefaultPaymentManagementService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration

    customer_repository: Callable[[], CustomerRepository] = providers.Factory(
        DjangoORMACustomerRepository
    )

    customer_management_service: Callable[[], CustomerManagementService] = providers.Factory(
        DefaultCustomerManagementService,
        repository=customer_repository
    )

    manager_repository: Callable[[], ManagerRepository] = providers.Factory(
        DjangoORMAManagerRepository
    )

    manager_management_service: Callable[[], ManagerManagementService] = providers.Factory(
        DefaultManagerManagementService,
        repository=manager_repository

    )

    room_repository: Callable[[], RoomRepository] = providers.Factory(
        DjangoORMARoomRepository
    )

    room_management_service: Callable[[], RoomManagementService] = providers.Factory(
        DefaultRoomManagementService,
        repository=room_repository
    )

    booking_repository: Callable[[], BookingRepository] = providers.Factory(
        DjangoORMABookingRepository
    )

    booking_management_service: Callable[[], BookingManagementService] = providers.Factory(
        DefaultBookingManagementService,
        repository=booking_repository
    )

    payment_repository: Callable[[], PaymentRepository] = providers.Factory(
        DjangoORMAPaymentRepository
    )

    payment_management_service: Callable[[], PaymentManagementService] = providers.Factory(
        DefaultPaymentManagementService,
        repository=payment_repository
    )

    guest_repository: Callable[[], GuestRepository] = providers.Factory(
        DjangoORMAGuestRepository
    )

    guest_management_service: Callable[[], GuestManagementService] = providers.Factory(
        DefaultGuestManagementService,
        repository=guest_repository
    )

    reservation_repository: Callable[[], ReservationRepository] = providers.Factory(
        DjangoORMAReservationRepository
    )

    reservation_management_service: Callable[[], ReservationManagementService] = providers.Factory(
        DefaultReservationManagementService,
        repository=reservation_repository
    )


hotel_service_provider = Container()
