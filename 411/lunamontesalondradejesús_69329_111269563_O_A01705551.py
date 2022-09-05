# Alondra de Jesús Luna Montes (A01705551)
import math

def sector (radio, ángulo):
    res = (math.pi*math.pow(radio,2)*ángulo)/360
    return res

def eclipse(a,b):
    res = math.pi*a*b
    return res

def paralelogramo(a,h):
    res = a*h
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Dame una opción: "))  
    if opcion == 1:
        radio = float(input("Dame el radio: "))
        ángulo = float(input("Dame el ángulo: "))
        res = sector(radio, ángulo)
        print("La superficie del sector circuclar es: %.2f" % (res))  
        
    elif opcion == 2:
        a = float(input("Dame el radio a: "))
        b = float(input("Dame el radio b: "))
        res = eclipse(a,b)
        print("La superficie del elipse es: %.2f" % (res))
        
    elif opcion == 3:
        a = float(input("Dame el lado a: "))
        h = float(input("Dame la altura h: "))
        res = paralelogramo(a,h)
        print("La superficie del paralelogramo es: %.2f" % (res))
        
        
    elif opcion == 4:
        print("Adiós")
    else:
        print("Opción inválida")
    

main()