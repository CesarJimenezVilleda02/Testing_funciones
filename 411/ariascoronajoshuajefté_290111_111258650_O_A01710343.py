#Joshua Jefté Arias Corona A01710343
import math

def sector(radio, angulo):
    res = math.pi * radio ** 2 * angulo / 360
    return res
    
def elipse(a, b):
    res = math.pi * a * b
    return res

def paralelogramo(a, h):
    res = a * h
    return res

def superficies():
    print("1. Sector")
    print("2. Elipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Introduce una opción: "))
    if opcion == 1:
        r = float(input("Ingresar radio del sector: "))
        a = float(input("Ingresar angulo del sector: "))
        res = sector(r, a)
        print("El area del sector es de: %.2f" % res)
    elif opcion == 2:
        a = float(input("Ingresar radio a: "))
        b = float(input("Ingresar radio b: "))
        res =  elipse(a, b)
        print("El area del elipse es de: %.2f" % res)
    elif opcion == 3:
        a = float(input("Ingresar longitud (a): "))
        h = float(input("Ingresar altura (h): "))
        res = paralelogramo(a, h)
        print("El area de la figura es de: %.2f" % res)
    elif opcion == 4:
        print ("Adiós")
    else:
        print ("Opción_invalida")
    
        
main ()
