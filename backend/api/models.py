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


class BookingRoom(models.Model):
    room_number = models.IntegerField()
    room_capacity = models.IntegerField()
    booking_name = models.CharField(max_length=50)
    booking_check_in = models.DateField()
    booking_check_out = models.DateField()
    booking_person = models.IntegerField()
    booking_created_at = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=False)

    # user who is logged in can only update his booking one time only
    # if he has already updated his booking then he can't update it again
    def save(self, *args, **kwargs):
        # if user update a room one time return True on updated field
        if self.updated:
            raise ValueError("You can't update this room anymore.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_name
