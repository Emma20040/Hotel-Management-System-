from django.db import models

# Create your models here.
# model for hotel
class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=20)



class RoomType(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False) #standard, delux 
    description = models.TextField(max_length=1000)
    price_per_night = models.DecimalField(decimal_places=2, blank=False, max_digits=10)
    capacity = models.IntegerField()


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, blank=False)
    CurrentBookingID = models.IntegerField()


class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200, default="nan")
    laast_name = models.CharField(max_length=200, default="nan")
    date_of_birth = models.DateField(default="")
    address = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=20, blank=True, default="added after")
    email = models.EmailField(unique=True, blank=False, default="late@gmail.com")


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    price = models.BigIntegerField()


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    Booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amont = models.BigIntegerField()
    payment_method = models.CharField()
    payment_date = models.DateTimeField(auto_now=True)

