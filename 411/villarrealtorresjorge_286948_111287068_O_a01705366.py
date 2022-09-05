#Jorge Villarreal (a01705366)

import math
def sector(radio,angulo):
    SC= (math.pi*radio**2*angulo)/360
    return SC

def elipse(radio_a,radio_b):
    SE= math.pi*radio_a*radio_b
    return SE

def paralelogramo(longitud, altura):
    SP= longitud*altura
    return SP

def menu():
    print("1. Sector")
    print ("2. Elipse")
    print ("3. Paralelogramo")
    print("4. Salir")

def main():
    menu()
    opcion= int(input("Introduce una opcion: "))
    if opcion==1:
        o1=float(input("Dame el radio:"))
        o11=float(input("Dame el angulo:"))
        SC = sector(o1,o11)
        print("El area del sector es %.2f:" % (SC))
    elif opcion==2:
        o2= float(input("Dame el radio 1:"))
        o22= float(input("Dame el radio 2:"))
        SE= elipse(o2,o22)
        print("El area del sector es %.2f" % (SE))
    elif opcion==3:
        o3=float(input("Dame la longitud:"))
        o33= float(input("Dame la altura:"))
        SP=paralelogramo(o3,o33)
        print("El area del sector es %.2f" % (SP))
    elif opcion==4:
        print("Adios")
    else:
        print("Opcion invalida")
    
main()