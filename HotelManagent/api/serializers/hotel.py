from rest_framework import serializers
from booking.models import Hotel, Room, RoomType

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def validate_email(self, value):
        
        if Hotel.objects.filter(email=value).exists():
            raise serializers.ValidationError("A hotel with this email already exists.")
        return value
    
    def validate_phone(self, value):
        """Validate phone number format (basic)"""
        if not value.isdigit() and not any(c in '+-() ' for c in value):
            raise serializers.ValidationError("Invalid phone number format.")
        return value