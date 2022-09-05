# Cristopher Moreno Perales A01706386

import math

def sector(radio, angulo):
    superficie = math.pi * radio ** 2 * angulo / 360
    return superficie

def elipse(a, b):
    superficie = math.pi * a * b
    return superficie

def paralelogramo(a, h):
    superficie = a * h
    return superficie

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        r = float(input("Dame el radio: "))
        a = float(input("Dame el ángulo: "))
        s = sector(r, a)
        print("La superficie es igual a %.2f u^2" % s)
    elif opcion == 2:
        ra = float(input("Dame el radio a: "))
        rb = float(input("Dame el radio b: "))
        s = elipse(ra, rb)
        print("La superficie es igual a %.2f u^2" % s)
    elif opcion == 3:
        la = float(input("Dame la longitud: "))
        ah = float(input("Dame la altura: "))
        s = paralelogramo(la, ah)
        print("La superficie es igual a %.2f u^2" % s)
    elif opcion == 4:
        print("Adiós")
    else:
        print("Opción inválida")
        
main()