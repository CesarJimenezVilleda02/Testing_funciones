
"""
Julio Cesar  Canseco Castro
 
 Algoritmo
 1.solicitar el numero de opcion
 2.1.  (opcion numero 1) 
 2.2 solicitar el valor del radio
 2.3. solicitar el valor del angulo
 2.4. desplegar el valor de la superficie de la figura 
 3.1. (opcion numero 2) 
 3.2. solicitar el valor de radio a
 3.3. solciitar el valor de radio b
 3.4. desplegar el valor de la superficie de la figura
 4.1. (opcion 3) 
 4.2. solicitar el valor del lado a 
 4.3. solicitar el valor de la altura 
 4.4. desplegar el valor de  la superficie de la figura 
"""
import math
from tkinter.ttk import LabeledScale
def sector(a,r):
 s=(math.pi*r**2*a)/360
 return s

def eclipse(a,b):
    s=math.pi*a*b
    return s

def paralelogramo(a,h):
    s=a*h
    return s

def superficies():
    print("1. sector")
    print("2. eclipse ")
    print("3. paralelogramo")
    print("4. Salir")


def main():
    superficies()
    op=int(input("Ingresa una opcion: "))
    if op==1:
        ang=float(input("Ingresa el valor del angulo: "))
        rad=float(input("Ingresa el valor del radio: "))
        y=sector(ang,rad)
        print("El valor de la superficie es:", y)

    if op==2:
        lada=float(input("Ingresa el valor del lado a: "))
        ladb=float(input("Ingresa el valor del lado b: "))
        y=eclipse(lada,ladb)
        print("El valor de la superficie es:", y)

    if op==3:
        ladaa=float(input("Ingresa el valor del lado a: "))
        alt=float(input("Ingresa el valor de la altura: "))
        y=sector(ladaa,alt)
        print("El valor de la superficie es:", y)

    if op==4:
     print("Hasta luego")

    else:
        print("Opcion invalida ")



main()
