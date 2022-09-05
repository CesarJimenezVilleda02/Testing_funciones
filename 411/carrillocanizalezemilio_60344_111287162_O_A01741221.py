# Emilio Carrillo Canizalez
import math
def sector(radio, angulo):
    res = (math.pi * radio**2 * angulo) / 360
    return res

def eclipse(a, b):
    res = (math.pi * a * b)
    return res

def paralelogramo(a, h):
    res = (a * h)
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main():
    superficies()
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        radio = float(input("Dame el radio: "))
        angulo = float(input("Dame el valor del ángulo: "))
        res = sector(radio, angulo)
        print("El valor del sector es %.2f" % (res))
    elif opcion == 2:
        a = float(input("Dame el valor del radio a: "))
        b = float(input("Dame el valor del radio b: "))
        res = eclipse(a, b)
        print("La superficie del eclipse es %.2f" % (res))
    elif opcion == 3:
        a = float(input("Dame el valor de la longitud a: "))
        h = float(input("Dame el valor de la altura: "))
        res = paralelogramo(a, h)
        print("La superficie del paralelogramo es %.2f" % (res))
    elif opcion == 4:
        print("Adiós")
    else:
        print("Opción invalida")
        
main()

        
        
    
    
    

