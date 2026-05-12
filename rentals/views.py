from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Car # Assuming you have a Booking model too

def index(request):
    # 1. Handle Admin Login
    if request.method == "POST" and 'login_btn' in request.POST:
        un = request.POST.get('un')
        ps = request.POST.get('ps')
        user = authenticate(request, username=un, password=ps)
        if user is not None:
            login(request, user)
            return redirect('index')

    # 2. Handle Logout
    if 'logout' in request.GET:
        logout(request)
        return redirect('index')

    cars = Car.objects.all()
    # If you have a Booking model, add this line:
    # bookings = Booking.objects.all() 
    
    return render(request, 'rentals/index.html', {
        'cars': cars,
        # 'bookings': bookings # Uncomment this if you have bookings
    })