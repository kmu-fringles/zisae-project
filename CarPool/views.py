from django.shortcuts import render, get_object_or_404,redirect
from .models import CarPool
from django.utils import timezone
# Create your views here.


def carpool(request):
    carpools=CarPool.objects.all()
    return render(request,'CarPool/home.html', {'carpools' : carpools})

def detail(request, carpool_id) :
    carpool = get_object_or_404(CarPool,pk=carpool_id)
    return render(request,'CarPool/detail.html', {'carpool' : carpool})

def new(request):
    return render(request,'CarPool/new.html')

def create(request):
    new_car=CarPool()
    new_car.title = request.POST['title']
    new_car.writer = request.POST['writer']
    new_car.pub_date = timezone.datetime.now()
    new_car.body = request.POST['content']
    new_car.save()
    return redirect('carpool_home')

def delete(request, delete_car_id):
    delete_car = get_object_or_404(CarPool, pk = delete_car_id)
    delete_car.delete()
    return redirect('carpool_home')

def edit(request, edit_car_id):
    edit_car = get_object_or_404(CarPool, pk = edit_car_id)
    return render(request,'CarPool/edit.html',{'carpool':edit_car})

def update(request, update_car_id):
    update_car=get_object_or_404(CarPool,pk=update_car_id)
    update_car.title = request.POST['title']
    update_car.writer = request.POST['writer']
    update_car.body = request.POST['content']
    update_car.save()
    return redirect('detail', update_car_id)

def search(request):
    q=request.GET['q']
    ans = Blog.objects.filter(title=q)
    return render(request, 'CarPool/search.html', {'q':q, 'ans':ans})