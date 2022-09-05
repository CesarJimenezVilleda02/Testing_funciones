#A01705886 Diego Antonio Veloz Briones

import math




def sector(radio,angulo):
    return (math.pi*(radio**2)*angulo)/360
    
def elipse(a,b):
    return math.pi*a*b

def paralelogramo(a,h):
    return a*h

def superficies():
    print("1.-Sector")
    print("2.-Elipse")
    print("3.-Paralelogramo")
    print("4.-Salir")



def main():
    superficies()
    opcion=int(input("Introduce una opcion:"))
    if opcion==1:
        radio= float(input("Introduce el radio:"))
        angulo= float(input("Introduce el angulo:"))
        sec=sector(radio,angulo)
        print("%.2f es el area del sector"%sec)
    elif opcion==2:
        a= float(input("Introduce el radio a:"))
        b= float(input("Introduce el radio b:"))
        elip=elipse(a,b)
        print("%.2f es el area de la elipse"%elip)
    elif opcion==3:
        a= float(input("Introduce la base:"))
        b= float(input("Introduce la altura:"))
        para=paralelogramo(a,b)
        print("%.2f es el area de la elipse"%para)
    elif opcion==4:
        print("Adios")
    else:
        print("Error")
main()