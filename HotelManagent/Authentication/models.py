from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username= None
    email = models.EmailField(_("email address"),unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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
    first_name = models
