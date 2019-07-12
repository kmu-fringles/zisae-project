from django.shortcuts import render, get_object_or_404, redirect
from .models import LostAndFound
from django.utils import timezone


# Create your views here.
def home(request) :
    losts = LostAndFound.objects
    return render(request, 'lostandfound/home.html', {'losts' : losts})

def detail(request, lost_id) :
    lost_detial = get_object_or_404(LostAndFound, pk = lost_id)
    return render(request, 'lostandfound/detail.html', {'lost': lost_detial})

def new(request) :
    return render(request, 'lostandfound/new.html')

def create(request) :
    lost = LostAndFound()
    lost.title = request.GET['title']
    lost.writer = request.GET['writer']
    lost.pub_date = request.GET['pub_date']
    lost.body = request.GET['body']
    lost.image= request.GET['image']
    lost.save()
    return redirect('/lostandfound/'+str(lost.id))

def delete(request, lost_id) :
    delete_lost = LostAndFound.objects.get(id=lost_id)
    delete_lost.delete()
    return redirect('lostandfound_home')

def edit(request, lost_id) :
    edit_lost = LostAndFound.objects.get(id = lost_id)
    return render(request, 'lostandfound/edit.html', {'lost': edit_lost})

def update(request, lost_id) :
    update_lost = LostAndFound.objects.get(id = lost_id)
    update_lost.title = request.POST['title']
    update_lost.writer = request.POST['writer']
    update_lost.pub_date = request.POST['pub_date']
    update_lost.body = request.POST['body']
    update_lost.save()
    return redirect('lostandfound_home')
