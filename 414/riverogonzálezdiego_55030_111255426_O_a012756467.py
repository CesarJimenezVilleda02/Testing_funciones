# Diego Rivero González (A01275646)
import math

def sector(r, a):
    res = (math.pi * r**2 * a) / 360
    return res

def eclipse(a, b):
    res = math.pi * a * b
    return res

def paralelograma(a, h):
    res = a * h
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("2. Paralelograma")
    print("3. Salir")
    
def main():
    superficies()
    opcion = int(input("Dame una opción: "))
    if opcion == 1:
        r = float(input("Introduce el valor del radio: "))
        a = float(input("Introduce el valor del angulo:"))
        res = sector(r, a)
        print("sector es %.2f" % (res))
    elif opcion == 2:
        a = float(input("Introduce el valor a: "))
        b = float(input("Introduce el valor b: "))
        res = eclipse(a, b)
        print("El eclipse es %.2f" % (res))
    elif opcion == 3:
        a = float(input("Introduce el valor a: "))
        h = float(input("Introduce el valor h: "))
        res = paralelograma(a, h)
        print("EL paralelograma es %.2f" % (res))
    elif opcion == 4:
        print("Salir")  
    else:
        print("Opción inválida")
        
main()

