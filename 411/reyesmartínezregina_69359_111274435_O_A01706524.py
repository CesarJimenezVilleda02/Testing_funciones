# Regina Reyes A01706524

"""Estoy 99% segura de que mencionó que esta tarea se hacía sin algoritmo
así que ojalá la memoria no me esté engañando
bonito día miss jajaja"""

import math
def sector(radio, angulo): #esta función regresa la superficie de un sector
    sector_S=(math.pi*(radio**2)*angulo)/360
    return sector_S

def eclipse(a,b): #regresa la superficie de la eclipse
    Eclipse_S=math.pi*a*b
    return Eclipse_S

def paralelogramo(a,h):#regresa superficie del paralelogramo
    Paralelo_S=a*h
    return Paralelo_S

def superficies(): #menú
    print('1. Sector')
    print('2. Eclipse')
    print('3. Paralelogramo')
    print('4. Salir')

def main (): #code run
    superficies()
    opcion=int(input("dame una opción: "))
    if opcion == 1:
        rad = float(input("Dame el radio: "))
        ang = float(input("Dame el ángulo: "))
        res=sector(rad,ang)
        print("La superficie del sector es %.2f" % res)

    elif opcion == 2:
        var_a=float(input("Dame el radio A: "))
        var_b=float(input("Dame el radio B: "))
        res=eclipse(var_a,var_b)
        print("La superficie de la eclipse es %.2f" % res)

    elif opcion == 3:
        var_a = float(input("Dame la longitud: "))
        var_h = float(input("Dame el valor de la altura: "))
        res = paralelogramo(var_a, var_h)
        print("La superficie del paralelogramo es %.2f" % res)

    elif opcion == 4:
        print("Adiós")
    else:
        print("Opción invalida!!!")

main()