from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'), #Ruta raiz de la API
]