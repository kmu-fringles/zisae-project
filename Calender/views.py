from django.shortcuts import render

# Create your views here.
def real_home(request) :
    return render(request, 'real_home.html')

def home(request) :
    return render(request, 'calender/home.html')
