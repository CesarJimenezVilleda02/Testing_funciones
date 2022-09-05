# Karen Corona (A01707594)
import math

def sector(radio,angulo):
    sup_sector = (math.pi * radio**2 * angulo) / 360
    return sup_sector

def eclipse(a,b):
    sup_eclipse = math.pi * a * b
    return sup_eclipse

def paralelogramo(a,h):
    sup_paralelogramo = a * h
    return sup_paralelogramo

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        radio = float(input("Introduce el radio: "))
        angulo = float(input("Introduce el angulo: "))
        s1 = sector(radio,angulo)
        print("La superficie del sector es: %.2f" % (s1))
    elif opcion == 2:
        a = float(input("Introduce el valor del radio a: "))
        b = float(input("Introduce el valor del radio b: "))
        s2 = eclipse(a,b)
        print("La superficie de la eclipse es: %.2f" % (s2))
    elif opcion == 3:
        a = float(input("Introduce la longitud: "))
        h = float(input("Introduce la altura: "))
        s3 = paralelogramo(a,h)
        print("La superficie del paralelogramo es: %.2f" % (s3))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_invalida")
        
main()
