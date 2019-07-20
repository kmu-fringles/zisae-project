from django.contrib import admin
from django.urls import path
import Calender.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Calender.views.home, name="calender_home"),
    path('<int:reservation_id>/', Calender.views.detail, name="detail"),
    path('new/', Calender.views.new, name="new"),
    path('create/', Calender.views.create, name="create"),
]
