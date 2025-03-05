# models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta 
from django.utils import timezone

class ParkingSpot(models.Model):
    BIKE = 'bike'
    CAR = 'car'
    EV_CAR = 'ev_car'
    
    SPOT_TYPES = [
        (BIKE, 'Bike Parking'),
        (CAR, 'Car Parking'),
        (EV_CAR, 'Car Parking (EV)'),
    ]
    
    spot_type = models.CharField(max_length=10, choices=SPOT_TYPES)
    spot_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_spot_type_display()} - {self.spot_number}"

    def check_availability(self):
        current_time = timezone.now()
        active_reservations = self.reservation_set.filter(start_time__lte=current_time, start_time__gte=current_time - models.F('duration'))
        return not active_reservations.exists()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(hours=1))

    def end_time(self):
        return self.start_time + self.duration

    def time_left(self):
        return max(self.end_time() - timezone.now(), timedelta(0))
