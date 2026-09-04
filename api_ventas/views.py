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

def error404View(request, exception):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>PÁGINA NO ENCONTRADA (ERROR 404)</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
            h1 { color: #d9534f; }
            a { text-decoration: none; color: #0275d8; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>PÁGINA NO ENCONTRADA (ERROR 404)</h1>
        <p>La pagina que estas buscando no existe. Por favor, verifica la URL.</p>
        <p><a href="/">Volver a la página de inicio</a></p>
    </body>
    </html>
    """
    return HttpResponse(html, status=404)