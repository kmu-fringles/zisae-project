from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Dating


# Create your views here.
def d_home(request):
    blogs= Dating.objects
    return render(request,'Dating/home.html',{'blogs':blogs})

def new(request):
    return render(request, 'Dating/new.html')


def detail(request, dating_id):
    dating_detail = get_object_or_404(Dating, pk=dating_id)
    return render(request, 'Dating/detail.html', {'dating': dating_detail})

def create(request):
    dating = Dating()
    dating.title = request.GET['title']
    dating.body = request.GET['body']
    dating.pub_date = timezone.datetime.now()
    dating.save()
    return redirect('/dating/'+str(dating.id))

def delete(request, dating_id):
    delete_dating = get_object_or_404(Dating, pk=dating_id)
    delete_dating.delete()
    return redirect('dating_home')

def edit(request, dating_id):
    edit_dating = get_object_or_404(Dating, pk=dating_id)
    return render(request, 'Dating/edit.html', {'dating':edit_dating})

def update(request, dating_id):
    update_dating = Dating.objects.get(id=dating_id)
    update_dating.title = request.POST['title']
    update_dating.body = request.POST['body']
    update_dating.save()
    return redirect('dating_home')
