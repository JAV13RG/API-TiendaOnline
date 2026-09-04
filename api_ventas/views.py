from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request): #Pagina de bienvenida de la API
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>API TIENDA ONLINE</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Bienvenido a la API de la Tienda Online "Tiendita INACAP"</h1>
        <p>Sistema pensado para la gestion de ventas, sus pedidos y reportes.</p>
    </body>
    </html>
    """
    return HttpResponse(html)