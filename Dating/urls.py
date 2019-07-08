from django.contrib import admin
from django.urls import path
import Dating.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dating.views.d_home, name='d_home'),
]