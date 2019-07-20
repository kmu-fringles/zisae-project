from django.contrib import admin
from django.urls import path
import Dating.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Dating.views.d_home, name='dating_home'),
    path('new/', Dating.views.new, name='new'),
    path('create/', Dating.views.create, name='create'),
    path('<int:dating_id>/', Dating.views.detail, name='detail'),
    path('delete/<int:dating_id>/',Dating.views.delete, name='delete'),
    path('edit/<int:dating_id>/', Dating.views.edit, name='edit'),
    path('update/<int:dating_id>/', Dating.views.update, name='update'),
]