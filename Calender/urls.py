from django.contrib import admin
from django.urls import path
import Calender.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Calender.views.home, name="calender_home"),
]
