#Harper A01706121
import math
def sector(radio, angulo):
    sup_sector = (math.pi * radio ** 2 * angulo)/360
    return sup_sector
def eclipse(a, b):
    sup_eclipse = math.pi * a * b
    return sup_eclipse
def paralelogramo(a, h):
    sup_paralelogramo = a * h
    return sup_paralelogramo
def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
def main():
    superficies()
    op = int(input("Selecciona una opción:"))
    if op == 1:
        r = float(input("Introduce el radio:"))
        g = float(input("Introduce los grados:"))
        res = sector(r, g)
        print("Superficie del sector = %.2f" % (res))
    elif op == 2:
        la = float(input("Introduce el lado a:"))
        lb = float(input("Introduce el lado b:"))
        res = eclipse(la, lb)
        print("Superficie del eclipse = %.2f" % (res))
    elif op == 3:
        a = float(input("Introduce la longitud:"))
        h = float(input("Introduce la altura:"))
        res = paralelogramo(a, h)
        print("Superficie del paralelogramo = %.2f" % (res))
    elif op == 4:
        print("Salir")
    else:
        print("Ingrese una opción válida")
main()