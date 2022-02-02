from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Guest)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Manager)
admin.site.register(Booking)


