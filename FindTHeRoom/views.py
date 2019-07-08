from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Find
# Create your views here.

def home(request):
    finds = Find.objects
    return render(request,'FindTHeRoom/home.html',{'finds':finds})

def roomwrite(request):
    return render(request,'FindTHeRoom/roomwrite.html')

def create(request):
    find = Find()
    find.title = request.GET['title']
    find.body = request.GET['body']
    find.pub_date = timezone.datetime.now()
    find.save()
    return redirect('/findtheroom/find/'+ str(find.id))
    
def detail(request, find_id):
    find_detail= get_object_or_404(Find, pk=find_id)
    return render(request,'FindTHeRoom/detail.html',{'find': find_detail})