from django.contrib import admin
from django.urls import path
import FindTHeRoom.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', FindTHeRoom.views.home, name='findtheroom_home'),
    path('new/', FindTHeRoom.views.create,name='new'),
    path('update/<int:pk>', FindTHeRoom.views.update,name='update'),
    path('delete/<int:pk>', FindTHeRoom.views.delete,name='delete'),
    
]

