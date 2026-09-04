# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request): #Pagina de bienvenida de la API
    #Variables y tipos de datos
    nombreProyecto = "API TIENDA ONLINE - Tiendita INACAP"
    version = 1.0
    enMantenimiento = False

    #Estructuras de control
    if enMantenimiento:
        estadoHtml = "<p style='color: red;'><strong>ESTADO:</strong> En mantenimiento</p>"
    else:
        estadoHtml = "<p style='color: green;'><strong>ESTADO:</strong> Operativo</p>"

    #Integracion logica
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>{nombreProyecto}</title>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
            h1 {{ color: #333; }}
        </style>
    </head>
    <body>
        <h1>Bienvenido a {nombreProyecto} (v{version})</h1>
        <p>Sistema pensado para la gestion de ventas, sus pedidos y reportes.</p>
        {estadoHtml}
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