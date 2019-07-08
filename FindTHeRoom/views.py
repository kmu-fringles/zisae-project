from django.shortcuts import render

from .models import FindTHeRoom
# Create your views here.

 def home(request):
     return render(request,'FindTHeRoom/home.html')