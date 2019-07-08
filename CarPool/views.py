from django.shortcuts import render, get_object_or_404
from .models import CarPool
# Create your views here.


def carpool(request):
    carpools=CarPool.objects
    return render(request,'CarPool/CarPool.html',{'carpools':carpool})

def detail(request, carpool_id) :
    carpool_detail = get_object_or_404(CarPool,pk=carpool_id)
    return render(request,'CarPool/CarPool.html',{'carpool':carpool_detail})