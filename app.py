import math

def sector(radio, angulo):
    superficie = (math.pi * radio**2 * angulo) / 360
    return superficie

def eclipse(a, b):
    superficie = math.pi * a * b
    return superficie

def paralelogramo(a, h):
    res = a * h
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main():
    superficies()
    opcion = float(input("Dame el radio: "))
    if opcion == 1:
        radio = float(input("Dame el radio: "))
        angulo = float(input("Dame el angulo: "))
        res = sector(radio, angulo)
        print("El sector es de %.2f" % (res))
    elif opcion == 2:
        a = float(input("Dame el primer radio: "))
        b = float(input("Dame el segundo radio: "))
        res = eclipse(a, b)
        print("El eclipse es de %.2f" % (res))
    elif opcion == 3:
        a = float(input("Dame el lado: "))
        h = float(input("Dame la altura: "))
        res = paralelogramo(a, h)
        print("El paralelogramo es de %.2f" % (res))
    elif opcion == 4:
        print("Salir")
    else:
        print("Opción inválida")
    
