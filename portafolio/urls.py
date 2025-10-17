from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('contacto/', views.contacto, name='contacto'),
    path('certificaciones/', views.certificaciones, name='certificaciones'),
]
