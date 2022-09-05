# Emiliano Verduzco Mercado (A01709791)
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
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        r = float(input("Dame el radio: "))
        a = float(input("Dame el angulo: "))
        res = sector(r, a)
        print("Superficie del Sector= %.2f" % res)
    elif opcion == 2:
        a = float(input("Dame el radio a: "))
        b = float(input("Dame el radio b: "))
        res = eclipse(a, b)
        print("Superficie de la eclipse= %.2f" % res)
    elif opcion == 3:
        a = float(input("Dame el lado a: "))
        h = float(input("Dame la altura: "))
        res = paralelogramo(a, h)
        print("Superficie del Paralelograma= %.2f" % res)
    elif opcion == 4:
        print("Adios")
    else:
        print("Opción inválida")

main()         