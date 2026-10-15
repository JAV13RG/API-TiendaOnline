from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100) # Nombre de la categoria
    descripcion = models.TextField(blank=True, null=True) # Descripcion de la categoria

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre