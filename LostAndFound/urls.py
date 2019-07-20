from django.contrib import admin
from django.urls import path
import LostAndFound.views
from django.conf import settings
from django.conf.urls.static import static

app_name = "LostAndFound"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', LostAndFound.views.home, name='lostandfound_home'),
    path('<int:lost_id>/', LostAndFound.views.detail, name="detail" ),
    path('new/', LostAndFound.views.new, name="new"),
    path('create/', LostAndFound.views.create, name="create"),
    path('<int:lost_id>/delete/', LostAndFound.views.delete, name="delete"), 
    path('<int:lost_id>/edit/', LostAndFound.views.edit, name="edit"),
    path('<int:lost_id>/update/', LostAndFound.views.update, name="update"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

