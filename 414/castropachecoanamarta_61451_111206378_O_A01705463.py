# Ana Marta Castro Pacheco A01705463

import math

def sector(radio,angulo):
    s = (math.pi * radio**2 * angulo) / 360
    return s

def eclipse(a,b):
    s = math.pi * a * b
    return s

def paralelogramo(a,h):
    s = a * h
    return s

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main():
    superficies()
    opcion = int(input("Escribe el número de opción: "))
    if opcion == 1:
        r = float(input("Escriba el valor del radio: "))
        a = float(input("Escriba el valor del ángulo: "))
        res = sector(r, a)
        print("La superficie del sector de la figura con radio %.2f y ángulo %.2f es de %.2f." % (r, a, res))
    elif opcion == 2:
        r_a = float(input("Escriba el valor del radio a: "))
        r_b = float(input("Escriba el valor del radio b: "))
        res = eclipse(r_a, r_b)
        print("La superficie del sector de la figura con radio a %.2f y radio b %.2f es de %.2f." % (r_a, r_b, res))
    elif opcion == 3:
        a = float(input("Escriba el valor del lado a: "))
        h = float(input("Escriba el valor de la altura: "))
        res = paralelogramo(a, h)
        print("La superficie del sector de la figura con lado a %.2f y altura %.2f es de %.2f." % (a, h, res))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opción inválida")
        
main()