#ROGELIO RODRIGUEZ

import math

def sector(radio, angulo):
    s = (math.pi * radio**2 * angulo) / 360
    return s

def eclipse(a, b):
    s = math.pi * a * b
    return s

def paralelogramo(a, h):
    s = a * h
    return s

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Introduce una opcion: "))
    
    if opcion == 1:
        r = float(input("Dame el radio: "))
        g = float(input("Dame los grados: "))
        res = sector(r, g)
        print("El sector tiene superficie de: %.2f" %(res))
        
    elif opcion == 2:
        a = float(input("dame el valor de a: "))
        b = float(input("dame el valor de b: "))
        res = eclipse(a, b)
        print("El elipse tiene superficie de: %.2f" %(res))
        
    elif opcion == 3:
        a = float(input("Dame la longitud a: "))
        h = float(input("Dame la altura h: "))
        res = paralelogramo(a, h)
        print("El paralelogramo tiene superficie de: %.2f" %(res))
        
    elif opcion == 4:
        print("Adios.")
        
    else:
        print("Opcion invalida.")

main()