import sys

# NOs permite insertar el directoria anterior (".."), en la búsqueda de ficheros
sys.path.insert(1, "..")

# print(sys.path)



from saludos import Saludo

Saludo()