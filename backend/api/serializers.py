from rest_framework import serializers
from .models import HotelRoom, HotelRoomBooking


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoom
        fields = "__all__"

class HotelRoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomBooking
        fields = "__all__"