#Sebastian Soto Rivera A01710999

import math

def sector(radio, angulo):
    res = (math.pi * radio**2) * angulo / 360
    return res

def eclipse( radio_a, radio_b):
    res = math.pi * radio_a * radio_b
    return res

def paralelogramo(longitud_a, altura_h):
    res = longitud_a * altura_h
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelograma")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        r = float(input("Escribe el radio: "))
        a = float(input("Escribe el angulo: "))
        res = sector(r, a)
        print("El sector equivale a %.2f " % res)
    elif opcion == 2:
        a = float(input("Escribe el radio a: "))
        b = float(input("Escribe el radio b: "))
        res = eclipse(a, b)
        print("El eclipse equivale a %.2f " % res)
    elif opcion == 3:
        a = float(input("Escribe la longitud: "))
        h = float(input("Escribe la altura: "))
        res = paralelogramo(a, h)
        print("El paralelograma equivale a %.2f  " % res)
    elif opcion == 4:
        print("Adiós")
    else:
        print("Opción invalida")
main()