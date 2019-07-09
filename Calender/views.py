from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Reservation

# Create your views here.
def real_home(request) :
    return render(request, 'real_home.html')

def home(request) :
    reservations = Reservation.objects
    return render(request, 'calender/home.html', {'reservations' : reservations})

def detail(request, reservation_id) :
    reservation_detail = get_object_or_404(Reservation, pk=reservation_id)
    return render (request, 'calender/detail.html', {'reservation_detail' : reservation_detail})

def new(request) :
    return render(request, 'calender/new.html')

def create(request) :
    reservation = Reservation()
    reservation.team = request.GET['team']
    reservation.body = request.GET['body']
    reservation.save()
    # return redirect('/calender/' + str(reservation.id))
    return redirect('/calender/home')
