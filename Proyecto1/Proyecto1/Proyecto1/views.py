from django.http import HttpResponse
import datetime
import sqlite3

#Esta función es una vista, que devolverá una respuesta
#Hay que decir a que url hay que ir para ver esa vista (url.py)
def saludo (request):
    titulo = """
    <html>
        <body>
            <h1> 
                Este es el título de la página
            </h1>
        </body>
    </html>"""

    return HttpResponse (titulo)

def darAlta(nombres,apellidos,DNIs,contrasenias):
    print(contrasenia)

nombre = input("Inserta el nombre\n")
apellido = input("Inserta el apellido\n")
DNI = input("Inserta el DNI\n")
contrasenia = input("Inserta contrasenia\n")

darAlta(nombre,apellido,DNI,contrasenia)






