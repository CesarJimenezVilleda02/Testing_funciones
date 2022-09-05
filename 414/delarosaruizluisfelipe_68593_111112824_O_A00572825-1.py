#Luis Felipe de la Rosa Ruiz A00572825

import math

def calculo_sector(radio, angulo):
    sector = (math.pi * radio**2 * angulo) / 360
    return sector

def calculo_elipse(aradio, bradio):
    elipse = math.pi * aradio * bradio
    return elipse

def calculo_paralelogramo(a, h):
    paralelogramo = a * h
    return paralelogramo

def superficies():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Introduzca una de las opciones: "))
    
    if opcion == 1:
        rad = float(input("Introduzca el radio: "))
        ang = float(input("Introduzca el ángulo: "))
        sect = calculo_sector(rad, ang)
        print("El sector para el círculo de radio %.2f y ángulo de %.2f es igual a %.2f" % (rad, ang, sect))
        
    elif opcion == 2:
        rada = float(input("Introduzca el radio A: "))
        radb = float(input("Introduzca el radio B: "))
        elip = calculo_elipse(rada, radb)
        print("El área del elipse con radio A de %.2f y radio B de %.2f es igual a %.2f" % (rada, radb, elip))
        
    elif opcion == 3:
        altu = float(input("Introduzca la altura: "))
        long = float(input("Introduzca la longitud: "))
        paral = calculo_paralelogramo(long, altu)
        print ("El paralelogramo con altura %.2f y longitud %.2f tiene un area de %.2f" % (altu, long, paral))
        
    elif opcion == 4:
        print("Adiós")
        
    else:
        print("Opcion_invalida")
        
main()
        