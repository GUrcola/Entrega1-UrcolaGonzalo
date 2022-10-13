from Familia import views
from django.urls import path
urlpatterns = [
    path('familiares/', views.ver_familia),
    path('crear-familiar/<str:nombre>/<str:apellido>/<int:edad>/', views.crear_familiar)
 ]
