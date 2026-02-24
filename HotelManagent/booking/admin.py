from django.contrib import admin
from booking.models import *

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hotel_id', 'name', 'address', 'email', 'phone')
