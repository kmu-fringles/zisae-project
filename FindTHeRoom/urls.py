from django.contrib import admin
from django.urls import path
import FindTHeRoom.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', FindTHeRoom.views.home, name='findtheroom_home'),
    path('roomwrite/',FindTHeRoom.views.roomwrite, name='findtheroom_roomwrite'),
    path('roomwrite/create/',FindTHeRoom.views.create,name='create'),
    path('find/<int:find_id>/',FindTHeRoom.views.detail,name='detail'),
    
]

