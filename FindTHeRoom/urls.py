from django.contrib import admin
from django.urls import path
import FindTHeRoom.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', FindTHeRoom.views.home, name='home'),
    path('new/', FindTHeRoom.views.create,name='new'),
    path('create/',FindTHeRoom.views.create,name='create'),
    path('update/<int:find_id>', FindTHeRoom.views.update,name='update'),
    path('delete/<int:find_id>', FindTHeRoom.views.delete,name='delete'),
    path('<int:find_id>',FindTHeRoom.views.detail,name="detail"),
    
]

