# Ana Paula Zetina (A01709739)

import math

def sector (radio, angulo):
    resultado = ((math.pi) *(radio**2) * (angulo)) / 360
    return resultado
def eclipse (ra, rb):
    eclip = math.pi * ra * rb
    return eclip
def paralelogramo (longitud, altura):
    paralel = longitud * altura
    return paralel

def superficies ():
    print ("1. Sector")
    print ("2. Eclipse")
    print ("3. Paralelogramo")
    print ("4. Salir")
    
def main():
    superficies ()
    opcion = int(input("Dame una opción: "))
    
    if opcion == 1:
        r = float(input("Dame el radio: "))
        a = float(input("Dame el ángulo: "))
        resultado = sector (r,a)
        print("%.2f" % (resultado))
    
    elif opcion == 2:
        raa = float(input("Dame el radio a: "))
        rab = float(input("Dame el radio b: "))
        eclip = eclipse (raa,rab)
        print("%.2f" % (eclip))
        
    elif opcion == 3:
        lon = float(input("Dame la longitud: "))
        alt = float(input("Dame la altura: "))
        paralel = paralelogramo (lon, alt)
        print("%.2f" % (paralel))  
    
    elif opcion == 4:
        print ("Adiós")
    else:
        print ("Opción inválida")
        
main ()