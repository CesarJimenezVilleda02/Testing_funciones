# Ulises Orlando Carrizalez Lerín (A01027715)

#Importar
import math

#Funciones
def sector(radio, angulo):
    res= (math.pi * angulo * math.pow(radio,2))/360
    return res

def eclipse(a, b):
    res= math.pi * a * b
    return res

def paralelogramo(a, h):
    res= a * h
    return res

def superficies():
    print("1. sector (radio, angulo)")
    print("2. eclipse (a, b) ")
    print("3. paralelogramo (a, h)")
    print("4. Salir")

#Final

def main():
    superficies ()
    op1= int(input("Dame un numero del indice: "))
    if op1 == 1:
        R= float(input("Dame el radio:"))
        A= float(input("Dame el angulo:"))
        res= sector(R,A)
        print("La superficie de la figura es %.2f"% (res))
        
    elif op1 == 2:
        A= float(input("Dame el radio a:"))
        B= float(input("Dame el radio b:"))
        res= eclipse(A,B)
        print("La superficie de la figura es %.2f"% (res))
             
    elif op1 == 3:
        A= float(input("Dame el lado a:"))
        H= float(input("Dame el altura b:"))
        res= paralelogramo(A,H)
        print("La superficie de la figura es %.2f"% (res))
     
    elif op1 == 4:
        print("Adios")
    else:
        print("opcion invalida")

main()