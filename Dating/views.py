from django.shortcuts import render

from .models import Dating


# Create your views here.
def d_home(request):
    return render(request,'Dating/d_home.html')

