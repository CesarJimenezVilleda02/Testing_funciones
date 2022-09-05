#Sebastian Valdez Carmona

import math

def sector(radio, angulo):
    res= (math.pi*radio**2 * angulo)/360
    return res

def elipse(a, b):
    res= math.pi*a*b
    return res

def paralelogramo(a, h):
    res= a*h
    return res

def superficies():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main():
    superficies()
    opcion=int(input("Dame una opcion:"))
    if opcion == 1:
        radio=float(input("Ingresa el radio:"))
        angulo=float(input("Ingresa el angulo:"))
        sec=sector(radio, angulo)
        print("La superficie del sector es %.2f" % (sec))
    elif opcion == 2:
        a=float(input("Ingrese el radio a:"))
        b=float(input("Ingrese el radio b:"))
        elip=elipse(a, b)
        print("La superficie de la elipse es %.2f" % (elip))
    elif opcion == 3:
        a=float(input("Ingrese la longitud a:"))
        h=float(input("Ingrese la altura h:"))
        parale= paralelogramo(a, h)
        print("La superficie del paralelogramo es %.2f" % (parale))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_invalida")

main()

    
    
    
