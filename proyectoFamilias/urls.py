from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiares/', views.ver_familia),
    path('crear-familiar/<str:nombre>/<str:apellido>/<int:edad>/', views.crear_familiar)
 ]
