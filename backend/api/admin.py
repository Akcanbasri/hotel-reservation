from django.contrib import admin
from .models import HotelRoom, HotelRoomBooking

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

@admin.register(HotelRoomBooking)
class HotelRoomBookingAdmin(admin.ModelAdmin):
    list_display = (
        "room_number",
        "room_floor",
        "room_capacity",
        "room_price",
        "room_type",
        "room_status",
        "room_description",
        "booking_name",
        "booking_email",
        "booking_phone",
        "booking_check_in",
        "booking_check_out",
        "booking_adults",
        "booking_children",
        "booking_infants",
        "booking_total",
        "booking_status",
        "booking_created_at",
    )
    list_filter = ("room_type", "room_status", "booking_status")
    search_fields = ("room_type", "room_status", "booking_status")
    ordering = ("room_type", "room_status", "booking_status")
    filter_horizontal = ()
    fieldsets = ()

    class Meta:
        model = HotelRoomBooking