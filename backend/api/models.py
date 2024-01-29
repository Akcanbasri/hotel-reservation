from django.db import models

# Create your models here.


class HotelRoom(models.Model):
    room_number = models.IntegerField()
    room_floor = models.IntegerField()
    room_capacity = models.IntegerField()
    room_price = models.IntegerField()
    room_type = models.CharField(max_length=50)
    room_status = models.CharField(max_length=50)
    room_description = models.CharField(max_length=200)

    def __str__(self):
        return self.room_type
    

class HotelRoomBooking(models.Model):
    room_number = models.IntegerField()
    room_floor = models.IntegerField()
    room_capacity = models.IntegerField()
    room_price = models.IntegerField()
    room_type = models.CharField(max_length=50)
    room_status = models.CharField(max_length=50)
    room_description = models.CharField(max_length=200)
    booking_name = models.CharField(max_length=50)
    booking_email = models.EmailField(max_length=50)
    booking_phone = models.IntegerField()
    booking_check_in = models.DateField()
    booking_check_out = models.DateField()
    booking_adults = models.IntegerField()
    booking_children = models.IntegerField()
    booking_infants = models.IntegerField()
    booking_total = models.IntegerField()
    booking_status = models.CharField(max_length=50)
    booking_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.booking_name

