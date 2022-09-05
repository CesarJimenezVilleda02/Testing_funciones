#Trinela Rodriguez A01706275

import math
def sector(radio,angulo):
    ans= (math.pi*(radio**2)*angulo)/360
    return ans
def eclipse(a,b):
    ans= math.pi*a*b
    return ans
def paralelogramo(a,h):
    ans= a*h
    return ans
def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
def main():
    superficies()
    op = int(input("Dame una opcion:"))
    if op == 1:
        radio = float(input("Dame el radio:"))
        angulo = float(input("Dame el angúlo:"))
        ans= sector(radio,angulo)
        print("La superficie del sector = %.2f" % (ans))

    elif op == 2:
        a = float(input("Dame el valor de a:"))
        b = float(input("Dame el valor de b:"))
        ans= eclipse(a,b)
        print("La superficie de la eclipse es: %.2f" %ans)
    elif op == 3:
        a = float(input("Dame el valor de a:"))
        h = float(input("Dame el valor de la altura:"))
        ans= paralelogramo(a,h)
        print("La superficie del paralelogramo: %.2f" %ans)
    elif op== 4:
        print("Adios")
    else:
        print("invalido")


main()
