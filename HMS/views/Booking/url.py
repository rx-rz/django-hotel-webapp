from django.urls import path
from HMS.views.Booking import booking_view

urlpatterns = [
    path('register', booking_view.create_booking, name='make_booking'),
    path('extend_booking', booking_view.extend_booking, name='extend_booking'),
    path('list_booking', booking_view.list_bookings, name='list_bookings'),
    path('list_active_booking', booking_view.list_active_bookings, name='list_active_bookings'),
    path('list_inactive_booking', booking_view.list_inactive_bookings, name='list_inactive_bookings'),
]
