#Rodrigo Manriquez López (A01710449)
""""
Algoritmo de Funciones
"""
import math

def Sector(r,a):
    sec= (math.pi * math.pow(r,2)*a)/360
    return sec


def Eclipse (a,b):
    sup= (math.pi * a * b)
    return sup

def Paralelogramo (a,h):
    s = a * h
    return s

def Menux():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. salir")
    
def main():
    
    Menux()
    
    opcion=int(input("Dame una opcion:"))
    if opcion ==1:
        r = float(input("Dame el radio:"))
        a= float(input("Dame el angulo:"))
        sec= (math.pi * math.pow(r,2)*a)/360
        print("La superficie del sector con radio=(%.1f) y con un el angulo solicitado es=(%.2f)" % (r,sec))
    
    elif opcion ==2:
        a= float(input("Dame el valor del radio a:"))
        b= float(input("Dame el valor del radio b:"))
        sup= (math.pi * a * b)
        print("La superficie de la eclipse es= %.2f" % sup)
    
    elif opcion ==3:
        a= float(input("Dame el valor del lado a:"))
        h= float(input("Dame la altura:"))
        s = a * h
        print("La superficie de el pararalelogramo es= %.2f" % s)
        
    elif opcion ==4:
        print("Adios regrese pronto")
        
    else:
        print("Opcion_invalida")
        
        
main()
    

    

