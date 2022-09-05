#Aldrick Tadeo (A01710105)

import math

def sector(radio, angulo):
    s_sector = (math.pi * radio**2 * angulo) / 360
    return s_sector

def elipse(a, b):
    s_elipse = math.pi * a * b
    return s_elipse

def paralelogramo(a, h):
    s_paral = a * h
    return s_paral

def superficies():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Introduce una opcion: "))
    
    if opcion == 1:
        r = float(input("Dame el radio: "))
        g = float(input("Dame los grados: "))
        res = sector(r, g)
        print("El sector tiene superficie de: %.2f" %(res))
        
    elif opcion == 2:
        a = float(input("dame el el valor de A: "))
        b = float(input("dame el el valor de B: "))
        res = elipse(a, b)
        print("La superficie de este elipse es: %.2f" %(res))
        
    elif opcion == 3:
        a = float(input("Entra la longitud A: "))
        h = float(input("Dame la altura: "))
        res = paralelogramo(a, h)
        print("El area del paralelogramo es: %.2f" %(res))
        
    elif opcion == 4:
        print("Adios.")
        
    else:
        print("Opcion invalida.")

main()