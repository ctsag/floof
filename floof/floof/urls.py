from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('menu/', include('menu.urls')),
    path('schedule/', include('schedule.urls'))
]
