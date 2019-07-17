from django.contrib import admin
from django.urls import path
import FindTHeRoom.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', FindTHeRoom.views.home, name='findtheroom_home'),
    
]

