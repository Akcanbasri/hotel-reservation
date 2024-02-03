from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HotelRoom, BookingRoom
from django.shortcuts import get_object_or_404
from .serializers import HotelRoomSerializer, BookingRoomSerializer

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
    serializer = BookingRoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_bookings(request):
    hotel_room_booking = BookingRoom.objects.all()
    serializer = BookingRoomSerializer(hotel_room_booking, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_booking_details(request, pk):
    booking_room = get_object_or_404(BookingRoom, pk=pk)
    serializer = BookingRoomSerializer(booking_room, many=False)
    return Response(serializer.data)


@api_view(["PUT"])
def update_booking(request, pk):
    # make updatede field True after updating the booking and user can't update it again
    booking_room = get_object_or_404(BookingRoom, pk=pk)
    serializer = BookingRoomSerializer(instance=booking_room, data=request.data)
    if serializer.is_valid():
        if booking_room.updated:
            return Response("You can't update this room anymore.")
        serializer.save()
    return Response(serializer.data)
