#Michelle Pacheco (A01709889)

import math

def sector(radio,angulo):
    S = (math.pi*(radio*radio)*angulo)/(360)
    return S

def eclipse(a,b):
    E = (math.pi*a*b)
    return E

def paralelogramo(a, h):
    P = (a*h)
    return P

def main():
   
    opcion = int(input("Introduce una opcion"))
    if opcion == 1:
        radio = float(input("Dame el radio"))
        angulo = float(input("Dame el angulo"))
        resultado_1 = sector(radio,angulo)
        print("El sector es: %.2f" % resultado_1)
    elif opcion == 2:
        a = float(input("Dme el valor de a"))
        b = float(input("Dame el valor de b"))
        resultado_2 = eclipse(a, b)
        print("La eclipse es: %.2f" % resultado_2)
    elif opcion == 3:
        a = float(input("Dme el valor de a"))
        h = float(input("Dame el valor de h"))
        resultado_3 = paralelogramo (a, h)
        print("El paralelogramo es: %.2f" % resultado_3)
    elif opcion == 4:
        print("Adios")
    else:
        print("opcion_invalida")
main()


    