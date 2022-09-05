#Sebastián López A01705842

import math

def sector(radio,angulo):
    res=(math.pi*radio**2*angulo)/360
    return res

def elipse(a,b):
    res=math.pi*a*b
    return res

def paralelogramo(a,h):
    res=a*h
    return res

def superficies():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main():
    superficies()
    opcion=int(input("Dame una opción\n"))
    if opcion==1:
        r=float(input("Dame el radio\n"))
        a=float(input("Dame el ángulo\n"))
        res=sector(r,a)
        print("El área de tu superficie es %.2f"%(res))
    elif opcion==2:
        r=float(input("Dame el radio 1\n"))
        r2=float(input("Dame el radio 2\n"))
        res=elipse(r,r2)
        print("El área de tu superficie es %.2f"%(res))
    elif opcion==3:
        l=float(input("Dame el valor del lado\n"))
        h=float(input("Dame la altura\n"))
        res=paralelogramo(l,h)
        print("El área de tu superficie es %.2f"%(res))
    elif opcion==4:
        print("Adiós")

    else:
        print("Opción Inválida")
        
        





main()
    
