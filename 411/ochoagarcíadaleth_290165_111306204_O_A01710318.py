#Daleth Ochoa Garcia (A01710318)

import math

def sector(radio,angulo):
    d= (math.pi * angulo * (radio**2))/360
    return d
def eclipse (a,b):
    d= (math.pi * a * b)
    return d
def paralelogramo (a,h):
    d= (a * h)
    return d

def problemas():
    print("1. sector (radio,angulo)")
    print("2. eclipse (a,b)")
    print("3. paralelogramo (a,h)")
    print("4. Salir")

def main():
    problemas ()
    opcion= int(input("Dame el número de índice: "))
    if opcion == 1:
        r= float(input("Dame el radio: "))
        a= float(input("Dame el angulo: "))
        res= sector(r,a)
        print("La superficie de la figura es %.2f"% (res))

    elif opcion == 2:
        a= float(input("Dame el valor para a: "))
        b= float(input("Dame el valor para b: "))
        res= eclipse(a,b)
        print("La superficie de la figura es %.2f"% (res))

    elif opcion == 3:
        a= float(input("Dame el valor para a: "))
        h= float(input("Dame el valor para h"))
        res= paralelogramo(a,h)
        print("La superficie de la figura es %.2f"% (res))

    elif opcion == 4:
        print("Adios")
    else:
        print("error")
main()

