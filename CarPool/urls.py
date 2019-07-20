from django.contrib import admin
from django.urls import path
import CarPool.views
app_name = "carpool"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', CarPool.views.carpool, name="carpool_home"),
    path('new/', CarPool.views.new, name="new"),
    path('create/',CarPool.views.create, name="create"),
    path('detail/<int:carpool_id>',CarPool.views.detail, name="detail"),
    path('delete/<int:delete_car_id>',CarPool.views.delete, name="delete"),
    path('edit/<int:edit_car_id>', CarPool.views.edit, name='edit'),
    path('update/<int:update_car_id>',CarPool.views.update,name="update"),
    path('search/',CarPool.views.search, name="search"),
]
