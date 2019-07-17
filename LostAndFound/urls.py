from django.contrib import admin
from django.urls import path
import LostAndFound.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', LostAndFound.views.home, name='lostandfound_home'),
    
]

