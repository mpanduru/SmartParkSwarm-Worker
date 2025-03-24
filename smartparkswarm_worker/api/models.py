from django.db import models

# Create your models here.

class ParkingLot(models.Model):
    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lot_name


class ParkingSpot(models.Model):
    uuid = models.UUIDField(unique=True)
    lot_uuid = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    spot_number = models.IntegerField(unique=True)
    is_occupied = models.BooleanField()

    def __str__(self):
        return self.spot_number
    
class VehicleEntry(models.Model):
    uuid = models.UUIDField(unique=True)
    spot_id = models.ForeignKey(ParkingSpot, on_delete=models.DO_NOTHING)
    license_plate = models.CharField(max_length=10)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(auto_now=False)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.license_plate} - {self.entry_time}"
    