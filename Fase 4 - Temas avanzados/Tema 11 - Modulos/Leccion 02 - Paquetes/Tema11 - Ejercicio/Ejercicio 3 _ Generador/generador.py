import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            n = int(input(mensaje))
        except:
            print ("Valor incorrecto. Introducir un número entre {} y {}.".format (ini,fin))
        else:
            if n>=ini and n<=fin:
                break
            else:
                print ("Valor incorrecto. Introducir un número entre {} y {}.".format (ini,fin))
    return n

def generador():
    numeros = leer_numero (1, 20, "¿Cuántos números quieres generar? [1-20]: ")
    modo = leer_numero (1,3, "¿Cómo quieres redondear los números?\n[1] Al alza\n[2] A la baja\n[3] Normal\nHa elegido: ")
    lista = []
    i = 0
    while i < numeros:
        n = random.uniform(0,100)
        i+=1
        if modo == 1:
            nr = math.ceil(n)
        if modo == 2:
            nr = math.floor (n)
        if modo == 3:
            nr = round (n)
        print ("Número\t{}\tRedondeo\t{}".format (n,nr))
        lista.append (nr)
        
    print(lista)
    
generador()