# Christian García (A01711004)

import math

def sector(radio, angulo):
    res = (math.pi * radio**2 * angulo) / 360
    return res
def eclipse(a, b):
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
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        radio = float(input("Dame el radio: "))
        angulo = float(input("Dame el angulo: "))
        print("La superficie de la figura es %.2f " % sector(radio, angulo))
    elif opcion == 2:
        a = float(input("Dame el radio mayor: "))
        b = float(input("Dame el radio menor: "))
        print("La superficie de la figura es %.2f " % eclipse(a, b))
    elif opcion == 3:
        a = float(input("Dame la longitud: "))
        h = float(input("Dame la altura: "))
        print("La superficie de la figura es %.2f " % paralelogramo(a,h))
    elif opcion == 4:
        print("Adiós")
    else:
        print("Opción Invalida")

main()