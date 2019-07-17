from django.contrib import admin
from django.urls import path
import CarPool.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', CarPool.views.carpool, name="carpool_home"),
]
