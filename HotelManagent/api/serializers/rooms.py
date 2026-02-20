from rest_framework import serializers
from booking.models import Room, RoomType


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

    def validate_price_per_night(self, value):
        """Ensure price is positive"""
        if value <= 0:
            raise serializers.ValidationError("Price per night must be greater than 0")
        return value

    def validate_room_capacity(self, value):
        if value < 1:
            raise serializers.ValidationError("room capacity must be alteas 1")
        
        if value> 15:
            raise serializers.ValidationError('room  capacity can not be more than 15 ')
        return value