# parkingapp/management/commands/update_spots.py
from django.core.management.base import BaseCommand
from parkingapp.models import ParkingSpot

class Command(BaseCommand):
    help = 'Update the availability of parking spots based on reservations'

    def handle(self, *args, **kwargs):
        spots = ParkingSpot.objects.all()
        for spot in spots:
            spot.is_occupied = not spot.check_availability()
            spot.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated parking spot availability'))
