from django.shortcuts import render,redirect,get_object_or_404
from .models import Find
from django.utils import timezone
from .forms import NewFind
# Create your views here.

def home(request):
    
    finds = Find.objects.all()
    return render(request,'FindTHeRoom/home.html',{'finds':finds})

def create(request):
    if request.method =="POST":
        form = NewFind(request.POST )
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return  redirect('findtheroom_home')


    else:
        form = NewFind()
        return render(request,'findtheroom/new.html',{'form':form})

def update(request,pk):

    find= get_object_or_404(Find,pk=pk)

    form=NewFind(request.POST, instance=find)

    if form.is_valid():
        form.save()
        return redirect('findtheroom_home')

    return render(request,'FindTHeRoom/new.html',{'form':form})   

def delete(request,pk):
    find = get_object_or_404(Find,pk=pk)
    find.delete()
    return  redirect('findtheroom_home')


