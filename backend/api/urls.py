from django.urls import path
from . import views

urlpatterns = [
    path("hotel-rooms/", views.get_hotel_rooms, name="get_hotel_rooms"),
    path("hotel-rooms/<str:pk>/", views.get_room_details, name="get_room_details"),
    path("book-room/", views.book_room, name="book_room"),
    path("bookings/", views.get_bookings, name="get_bookings"),
    path("bookings/<str:pk>/", views.get_booking_details, name="get_booking_details"),
    path("bookings/<str:pk>/update/", views.update_booking, name="update_booking"),
]
