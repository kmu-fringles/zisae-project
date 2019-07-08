from django.shortcuts import render

from .models import Dating


# Create your views here.
def d_home(request):
    blogs= Dating.objects
    return render(request,'Dating/home.html',{'blogs':blogs})

