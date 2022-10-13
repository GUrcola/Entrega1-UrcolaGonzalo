from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path ('Familia/', include('Familia.urls.py')),
    path('admin/', admin.site.urls),
 ]
