from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Iniciar el router
router = DefaultRouter()

# Registrar las vistas en el router
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'), #Ruta raiz de la API
    path('api/', include(router.urls)),
]