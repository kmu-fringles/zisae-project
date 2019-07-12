from django.contrib import admin
from django.urls import path
import LostAndFound.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', LostAndFound.views.home, name='lostandfound_home'),
    path('<int:lost_id>/', LostAndFound.views.detail, name="detail" ),
    path('new/', LostAndFound.views.new, name="new"),
    path('create/', LostAndFound.views.create, name="create"),
    
]

