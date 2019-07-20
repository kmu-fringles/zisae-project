"""underGround URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import Calender.views
<<<<<<< HEAD
import FindTHeRoom.views
import FindTHeRoom.urls
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> master


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Calender.views.real_home, name="real_home"),
    path('calender/', include('Calender.urls')),
    path('carpool/', include('CarPool.urls')),
    path('dating/', include('Dating.urls')),
    path('findtheroom/', include('FindTHeRoom.urls')),
    path('lostandfound/', include('LostAndFound.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

