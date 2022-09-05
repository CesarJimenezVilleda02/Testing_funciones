#Josue David Camacho Garcia (a01705627)
import math

def sector(radio , angulo):
    sec = (math.pi * radio ** 2 * angulo) / 360
    return sec

def eclipse(a , b):
    ecl = math.pi * a * b
    return ecl

def paralelogramo(a , h):
    parl = a * h
    return parl

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. salir")
    
def main ():
    superficies()
    opcion = int(input("Hola, ingresa un numero: "))
    if opcion == 1:
        radio = float(input("Dame el radio: "))
        angulo = float(input("Dame el angulo: "))
        res = sector(radio , angulo)
        print("El sector de tu circulo es %.2f" % (res))
    elif opcion == 2:
        radioa = float(input("Dame el radio a: "))
        radiob = float(input("Dame el radio b: "))
        res = eclipse(radioa , radiob)
        print("La superficie de tu eclipse es %.2f" % (res))
    elif opcion == 3:
        longitud = float(input("Dame la longitud: "))
        altura = float(input("Dame la altura: "))
        res = paralelogramo(longitud , altura)
        print("La superficie de tu paralelogramo es %.2f" % (res))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion invalida")
    
main()