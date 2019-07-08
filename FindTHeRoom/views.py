from django.shortcuts import render

from .models import Find
# Create your views here.

def home(request):
    return render(request,'FindTHeRoom/home.html')
    finds = Find.objects
    return render(request,'home.html',{'finds':finds})