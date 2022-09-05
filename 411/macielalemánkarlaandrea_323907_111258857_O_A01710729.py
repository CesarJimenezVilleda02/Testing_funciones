#Karla Maciel (A01710729)
import math

def sector(radio, grados):
    res = (math.pi * radio ** 2 * grados) / 360
    return res
def elipse(a, b):
    res = math.pi * a * b
    return res
def paralelogramo(a,h):
    res = a * h
    return res
def superficies():
    print("1.Sector")
    print("2.Elipse")
    print("3.Paralelogramo")
    print("4.Salir")

def main():
    superficies()
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        r = float(input("Dame el radio: "))
        g = float(input("Dame los grados: "))
        res = sector(r, g)
        print("La superfice es (%.1f), (%.1f) = %.2f" % (r, g, res))
    elif opcion == 2:
        a = float(input("Dame el lado a: "))
        b = float(input("Dame el lado b: "))
        res = elipse(a, b)
        print("La superfice es (%.1f), (%.1f) = %.2f" % (a, b, res))
    elif opcion == 3:
        a = float(input("Dame el lado a: "))
        h = float(input("Dame la h: "))
        res = paralelogramo(a, h)
        print("La superfice es (%.1f) * (%.1f) = %.2f" % (a, h, res))
    elif opcion == 4:
        print("Adiós")
    else:
        print("Opcion_invalida")
        
main()