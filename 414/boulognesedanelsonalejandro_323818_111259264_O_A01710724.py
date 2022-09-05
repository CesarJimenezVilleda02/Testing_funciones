#Nelson A. Boulogne Seda
import math
def sector(radio,angulo):
    res = (math.pi * radio ** 2 * angulo)/360
    return res
def eclipse(a,b):
    res = math.pi * a * b
    return res
def paralelogramo(a,h):
    res = a * h
    return res
def superficies_1 ():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelograma")
    print("4. Salir")

def main ():
    superficies_1()
    opcion = int(input("Elige el proceso que desea realizar "))
    if opcion == 1:
        rad = float(input("Ingrese el radio "))
        ang = float(input("Ingrese el angulo "))
        sec = sector(rad,ang)
        print("El sector es de %.2f" % (sec))
    elif opcion == 2:
        rada = float(input("Ingrese el radio a "))
        radb = float(input("Ingrese el radio b "))
        ec = eclipse(rada,radb)
        print("El eclipse es de %.2f" % (ec))
    elif opcion == 3:
        a = float(input("Ingrese la longitud "))
        h = float(input("Ingrese el altura "))
        par = eclipse(a,h)
        print("El paralelogramo es de %.2f" % (par))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion invalida")
main()