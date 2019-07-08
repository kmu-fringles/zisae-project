from django.contrib import admin
from django.urls import path
import FindTHeRoom.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find/', FindTHeRoom.views.home, name='findmain'),
    
]

