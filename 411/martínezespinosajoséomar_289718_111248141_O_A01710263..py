# José Omar Martínes Espinosa (A01710263)

import math

def sector(radio, angulo):
    res = (math.pi * radio**2 * angulo) / 360
    return res

def elipse(a, b):
    res = math.pi * a * b
    return res

def paralelogramo(a, h):
    res = a * h
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main():
    superficies()
    opcion = int(input("Digite el número de opción: "))   
    if opcion == 1:
        r = float(input("Deame el radio: "))
        a = float(input("Dame el ángulo: "))
        res = sector(r, a)
        print("El sector es %.2f" % (res))
        
    elif opcion == 2:
        radioA = float(input("Dame el radio A: "))
        radioB = float(input("Dame el radio B: "))
        res = elipse(radioA, radioB)
        print("La superficie de la elipse es %.2f" % (res))
        
    elif opcion == 3:
        ladoA = float(input("Dame el lado A: "))
        altura = float(input("Dame la altura: "))
        res = paralelogramo(ladoA, altura)
        print("La superficie del paralelogramo es %.2f" % (res))
    
    elif opcion == 4:
        print("Adiós")
        
    else:
        print("Opción_inválida")
        
main()        
        
    
    
        
        
        
        
        
        