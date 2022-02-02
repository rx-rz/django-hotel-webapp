from datetime import date
import uuid
from django.http import HttpRequest
from django.shortcuts import redirect, render

from HMS.models import Booking, Reservation, Customer, Guest
from HMS.service_provider import hotel_service_provider
from HMS.dto.BookingDto import *

room_types = {
    'Basic': 5000,
    'Deluxe': 10000,
    'Mega-Deluxe': 15000,
    'Presidential': 30000
}


def extend_booking(request):
    context = {
        'title': 'Extend Booking'
    }
    __extend_booking_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('home')
    return render(request, 'booking/extend_booking.html', context)


def create_booking(request):
    context = {
        'title': 'Make Booking'
    }

    __create_booking_if_post_method(request, context)
    if request.method == 'POST' and context['saved'] is True:
        return redirect('home')
    elif request.method == 'POST' and context['saved'] == 'Pay Now':
        return render(request, 'payment/make_payment.html', context)
    return render(request, 'booking/createbooking.html', context)


def __get_room_amount_by_room_type(room_type: str):
    for room in room_types:
        if room == room_type:
            result = room_types[room]
            return result
    return None


def __get_attribute_from_request(request: HttpRequest):
    make_booking_dto = CreateBooking()
    make_booking_dto.customer_email = request.POST['email']
    make_booking_dto.customer_phone_number = request.POST['phone_number']
    make_booking_dto.room_type = request.POST['room_type']
    make_booking_dto.check_in = request.POST['check_in']
    make_booking_dto.check_out = request.POST['check_out']
    make_booking_dto.payment_type = request.POST['payment_type']
    make_booking_dto.number_of_rooms = request.POST['number_of_rooms']
    return make_booking_dto


def __get_attribute_from_request_for_booking_listing(request: HttpRequest):
    term_dto = BookingTerm()
    term_dto.term = request.POST['term']
    return term_dto


def __get_attribute_from_request_for_booking_extension(request: HttpRequest):
    extend_booking_dto = ChangeCheckOut()
    extend_booking_dto.booking_reference = request.POST['booking_reference']
    extend_booking_dto.check_out = request.POST['check_out']
    return extend_booking_dto


def list_bookings(request):
    bookings = hotel_service_provider.booking_management_service().list_bookings()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/list_booking.html', context)


def list_inactive_bookings(request):
    bookings = hotel_service_provider.booking_management_service().list_active_bookings()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/list_inactive_bookings.html', context)


def list_active_bookings(request):
    bookings = hotel_service_provider.booking_management_service().list_inactive_bookings()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/list_active_bookings.html', context)


def __extend_booking_if_post_method(request, context):
    if request.method == 'POST':
        extend_request = __get_attribute_from_request_for_booking_extension(request)
        if extend_request:
            booking = hotel_service_provider.booking_management_service().get_booking_by_booking_reference(
                extend_request.booking_reference)
            extension_date = __date_maker(str(extend_request.check_out))
            check_out_date = __date_maker(str(booking.check_out))
            if booking and check_out_date < extension_date:
                booking.check_out = extension_date
                hotel_service_provider.booking_management_service().change_check_out_date(booking)
                context['saved'] = True
            else:
                context['saved'] = False
        else:
            context['saved'] = False


def __create_booking_if_post_method(request, context):
    if request.method == 'POST':
        booking = Booking()
        booking_request = __get_attribute_from_request(request)
        if booking_request:
            date_confirm = __confirm_date(booking_request.check_in, booking_request.check_out)
            if date_confirm is True:
                no_of_days_for_all_rooms = __payment_calculation(str(booking_request.check_in),
                                                                 str(booking_request.check_out),
                                                                 int(booking_request.number_of_rooms))
                price = __total_payment(no_of_days_for_all_rooms, booking_request.room_type)

                reservation = Reservation()
                guest = Guest()

                booking.booking_amount = price
                booking.check_in = booking_request.check_in
                booking.check_out = booking_request.check_out
                booking.payment_status = 'active'
                booking.number_of_rooms = booking_request.number_of_rooms

                booking.room_type = booking_request.room_type
                booking.booking_reference = __generate_booking_reference()
                booking.customer_email = booking_request.customer_email
                booking.customer_phone_number = booking_request.customer_phone_number
                booking.payment_type = booking_request.payment_type

                count = 0
                room_list = []
                while count < int(booking.number_of_rooms):
                    reservation.booking_reference = booking.booking_reference
                    reservation.room_number = __get_room(booking.room_type)
                    reservation.check_in = booking.check_in
                    reservation.check_out = booking.check_out
                    reservation.guest_name = booking.customer_email
                    count += 1
                    room_list.append(reservation.room_number)
                    hotel_service_provider.reservation_management_service().create_reservation(reservation)
                guest.name = booking.customer_email
                guest.booking_reference = booking.booking_reference
                guest.balance = booking.booking_amount
                guest.check_in = booking.check_in
                guest.check_out = booking.check_out
                guest.status = 'active'

                f1 = ""
                for i in room_list:
                    f1 += str(i) + "    "
                guest.room_numbers = f1
                booking.room_ids = f1
                hotel_service_provider.guest_management_service().create_guest(guest)
                if booking.payment_type == 'Pay On Arrival':
                    hotel_service_provider.booking_management_service().create_booking(booking)
                    context['saved'] = True
                elif booking.payment_type == 'Pay Now':
                    hotel_service_provider.booking_management_service().create_booking(booking)
                    user = hotel_service_provider.customer_management_service().customer_details(request.user.id)
                    if user is None:
                        context['saved'] = 'REGISTER WITH US TO BE ABLE TO ACCESS PAYMENT NOW'
                    context['saved'] = 'Pay Now'
                else:
                    context['saved'] = False

            else:
                context['saved'] = False

        else:
            context['saved'] = False

    else:
        context['saved'] = False


def __confirm_date(check_in: date, check_out: date):
    if check_in == check_out:
        return False

    if check_in > check_out:
        return False

    if check_in < check_out:
        return True


def __get_room(room_type: str):
    rooms = hotel_service_provider.room_management_service().list_rooms()
    for room in rooms:
        if room.room_type == room_type and room.room_status == 'inactive':
            room.room_status = 'active'
            hotel_service_provider.room_management_service().change_room_status(room)
            return room.room_number


def __payment_calculation(check_in: str, check_out: str, number_of_rooms: int):
    check_in_list = []
    check_out_list = []
    a = check_in.split('-')
    b = check_out.split('-')
    for i in a:
        check_in_list.append(int(i))
    for i in b:
        check_out_list.append(int(i))
    date1 = date(check_in_list[0], check_in_list[1], check_in_list[2])
    date2 = date(check_out_list[0], check_out_list[1], check_out_list[2])
    answer = (date2 - date1)
    price = int(answer.days) * number_of_rooms
    return price


def __date_maker(particular_date: str):
    if len(particular_date) <= 10:
        list1 = []
        a = particular_date.split('-')
        for i in a:
            list1.append(int(i))
        date1 = date(list1[0], list1[1], list1[2])
        return date1

    elif len(particular_date) > 10:
        new_date = particular_date[0:10]
        list1 = []
        a = new_date.split('-')
        for i in a:
            list1.append(int(i))
        date2 = date(list1[0], list1[1], list1[2])
        return date2


def __total_payment(payment: int, room_type: str):
    if room_type == 'Basic':
        return payment * 20000
    if room_type == 'Deluxe':
        return payment * 30000
    if room_type == 'Mega-Deluxe':
        return payment * 35000
    if room_type == 'Presidential':
        return payment * 50000


def __generate_booking_reference():
    a = uuid.uuid4().node
    reference = str(a).strip()
    return reference
