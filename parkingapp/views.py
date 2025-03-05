# parkingapp/views.py
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ParkingSpot, Reservation
from django.utils import timezone
from datetime import timedelta

@login_required
def home(request):
    bike_spots = ParkingSpot.objects.filter(spot_type='bike')
    car_spots = ParkingSpot.objects.filter(spot_type='car')
    ev_car_spots = ParkingSpot.objects.filter(spot_type='ev_car')
    return render(request, 'parkingapp/home.html', {'bike_spots': bike_spots, 'car_spots': car_spots, 'ev_car_spots': ev_car_spots})

@login_required
def spot_list(request, spot_type):
    spots = ParkingSpot.objects.filter(spot_type=spot_type)
    for spot in spots:
        spot.is_occupied = not spot.check_availability()
        spot.save()
    return render(request, 'parkingapp/spot_list.html', {'spots': spots})

@login_required
def reserve_spot(request, spot_id):
    spot = get_object_or_404(ParkingSpot, id=spot_id)
    if request.method == 'POST':
        hours = int(request.POST.get('hours'))
        minutes = int(request.POST.get('minutes'))
        duration = timedelta(hours=hours, minutes=minutes)
        reservation = Reservation(user=request.user, parking_spot=spot, duration=duration)
        reservation.save()
        spot.is_occupied = True
        spot.save()
        return redirect('home')
    return render(request, 'parkingapp/reserve_spot.html', {'spot': spot})

# def logout_view(request):
#     logout(request)
#     return redirect('login')