#Julieta GALVÁN A01705929
import math 
def superficie (radio, angulo):
    s=(math.pi*radio**2*angulo)/360
    return s
def elipse (a,b):
    eclipse=math.pi*a*b
    return eclipse
def paralelogramo (a,h):
    superficie=a*h
    return superficie
def superficies ():
    print("1. Sector")
    print("2. Eclipse")
    print("Paralelogramo")
    print("Salir")
def main ():
    superficies ()
    opcion=int(input("Dame una opción:   "))
    if opcion == 1:
        angulo=float(input("Dame el angulo:    "))
        radio=float(input("Dame el radio :   "))
        sector=superficie (radio, angulo)
        print("%.2f esta es la superficie" % (sector))
    elif opcion == 2:
        
        a=float(input("Dame A:   "))
        b=float(input("Dame B:    "))
        e=elipse (a,b)
        print("%.2f esta es la superficie del eclipse" % (e))
        
    elif opcion == 3:
        a= float(input("Dame A:  "))
        h=float(input("Dame b:    "))
        s=paralelogramo (a,h)
        print("%.2f esta es la superficie del paralelogramo" % (s))
        
    elif opcion == 4:
        print("adiós")
    else:
        print("Opción_invalida")
        
        
    
main()