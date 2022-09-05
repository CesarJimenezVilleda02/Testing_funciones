#María Jimena Reyes Sotomayor A01705490

import math

def sector (radio,angulo):
    resultado = ((math.pi)*(radio**2)*(angulo))/360
    return resultado

def elipse (a,b):
    resultado = math.pi*a*b
    return resultado

def paralelogramo (a,h):
    resultado = a*h
    return resultado

def superficies ():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main ():
    opcion = int(input("Dame una opción: "))
    if opcion==1:
        radio=float(input("Dame el radio: "))
        angulo=float(input("Dame el ángulo: "))
        resultado=sector(radio,angulo)
        print("El resultado es: %.2f" %resultado)
    elif opcion==2:
        radioA=float(input("Dame el radio a: "))
        radioB=float(input("Dame el radio b: "))
        resultado=elipse(radioA,radioB)
        print("El resultado es: %.2f" %resultado)
    elif opcion==3:
        altura=float(input("Dame la altura: "))
        longitud=float(input("Dame la longitud: "))
        resultado=paralelogramo(altura,longitud)
        print("El resultado es: %.2f" %resultado)
    elif opcion==4:
        print("Adiós")
    else:
        print("La opción no es válida")
        
main()