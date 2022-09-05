#Hector Esteban Perez Bonifant (A01710834)
import math

def sector(r, a):
    superficie = (math.pi * r**2 * a) / 360
    return superficie

def eclipse(a, b):
    superficie = math.pi * a * b
    return superficie

def paralelogramo(a, h):
    superficie = a * h
    return superficie

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        r = float(input("Dame el radio: "))
        a = float(input("Dame el valor del angulo: "))
        superficie = sector(r, a)
        print("Un sector con radio de %.1f y un angulo de %.1f tiene una superficie de %.2f" % (r, a, superficie))
    elif opcion == 2:
        a = float(input("Dame el valor del radio a: "))
        b = float(input("Dame el valor del radio b: "))
        superficie = eclipse(a, b)
        print("Un eclipse con radio a de %.1f y un radio b de %.1f tiene una superficie de %.2f" % (a, b, superficie))
    elif opcion == 3:
        a = float(input("Dame el valor del lado a: "))
        h = float(input("Dame el valor de la altura: "))
        superficie = paralelogramo(a, h)
        print("Un paralelogramo con lado a de %.1f y una altura h de %.1f tiene una superficie de %.2f" % (a, h, superficie))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion invalida")
    
    
main()