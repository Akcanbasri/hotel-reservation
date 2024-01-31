from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HotelRoom, HotelRoomBooking
from django.shortcuts import get_object_or_404
from .serializers import HotelRoomSerializer, HotelRoomBookingSerializer
from rest_framework import status

# Create your views here.


@api_view(["GET"])
def get_hotel_rooms(request):
    hotel_rooms = HotelRoom.objects.all()
    serializer = HotelRoomSerializer(hotel_rooms, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_room_details(request, pk):
    hotel_room = get_object_or_404(HotelRoom, pk=pk)
    serializer = HotelRoomSerializer(hotel_room, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def book_room(request):
    serializer = HotelRoomBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_bookings(request):
    hotel_room_booking = HotelRoomBooking.objects.all()
    serializer = HotelRoomBookingSerializer(hotel_room_booking, many=True)
    return Response(serializer.data)


# user who is logged in can only update his booking one time only
@api_view(["PUT"])
def update_booking(request, pk):
    hotel_room_booking = HotelRoomBooking.objects.get(id=pk)
    serializer = HotelRoomBookingSerializer(
        instance=hotel_room_booking, data=request.data
    )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
