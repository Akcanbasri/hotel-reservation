from django.contrib import admin
from .models import HotelRoom, BookingRoom

# Register your models here.


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = (
        "room_number",
        "room_floor",
        "room_capacity",
        "room_price",
        "room_type",
        "room_status",
        "room_description",
    )
    list_filter = ("room_type", "room_status")
    search_fields = ("room_type", "room_status")
    ordering = ("room_type", "room_status")
    filter_horizontal = ()
    fieldsets = ()

    class Meta:
        model = HotelRoom


@admin.register(BookingRoom)
class BookingRoomAdmin(admin.ModelAdmin):
    list_display = (
        "room_number",
        "room_capacity",
        "booking_name",
        "booking_check_in",
        "booking_check_out",
        "booking_person",
        "booking_created_at",
        "updated",
    )
    list_filter = ("booking_name", "booking_check_in", "booking_check_out")
    search_fields = ("booking_name", "booking_check_in", "booking_check_out")
    ordering = ("booking_name", "booking_check_in", "booking_check_out")
    filter_horizontal = ()
    fieldsets = ()

    class Meta:
        model = BookingRoom
