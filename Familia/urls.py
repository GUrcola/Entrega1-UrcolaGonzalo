from Familia import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='Index'), 
    path('familiares/', views.ver_familia, name='ver familia'),
    path('crear-familiar/<str:nombre>/<str:apellido>/<int:edad>/', views.crear_familiar, name='crear familiar'),
    path('about/', views.About, name='About')
 ]
