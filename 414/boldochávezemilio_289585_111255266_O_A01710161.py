#Emilio Boldo Chávez A01710161
import math

def sector(radio, angulo):
    res= ((math.pi)*(radio**2)*(angulo))/360
    return res
def elipse(a,b):
    res= math.pi*a*b
    return res
def paralelogramo(a,h):
    res= a*h
    return res
def superficies():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")
def main():
    superficies() 
    opcion= int(input("Dame una opcion:"))
    if opcion==1:
        r= float(input("Dame el radio "))
        a= float(input("Dame el ángulo"))
        res = sector(r,a)
        print ("Superficie del sector es:%.2f" % (res))
    elif opcion==2:
        a=float(input("Escribe el valor del radio a"))
        b=float(input("Escribe el valor del radio b"))
        res= elipse(a,b)
        print ("El área de la elipse es: %.2f" % (res))
    elif opcion==3:
        a=float(input("Escribe el valor del lado a"))
        h=float(input("Escribe la altura"))
        res=paralelogramo(a,h)
        print("El área del paralelogramo es: %.2f" % (res))
    elif opcion==4:
        print("salir")
    else:
        print("opcion_invalida")
       
main()
    