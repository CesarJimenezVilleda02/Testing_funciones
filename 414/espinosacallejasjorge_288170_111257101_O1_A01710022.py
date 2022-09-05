# Jorge Espinosa Callejas (A01710022)

import math

def sector(radio, angulo) :
    res = (math.pi * radio**2 * angulo) / 360
    return res

def eclipse(a, b) :
    res = math.pi * a * b
    return res

def paralelogramo(a, h) :
    res = a * h
    return res

def superficies() :
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")

def main() :
    superficies()
    opcion = int(input("Eliga la opción para calcular su superficie: "))
    
    if opcion == 1 :
        r = float(input("Dame el radio del sector: "))
        an = float(input("Dame el ángulo del sector: "))
        res = sector(r, an)
        print("Superficie del sector: %.2f" % (res))
    
    elif opcion == 2 :
        r_mayor = float(input("Ingresa el radio mayor: "))
        r_menor = float(input("Ingresa el radio menor: "))
        res = eclipse(r_mayor, r_menor)
        print("La superficie del eclipse: %.2f" % (res))
    
    elif opcion == 3 :
        lado = float(input("Ingresa el valor del lado (horizontal): "))
        altura = float(input("Ingresa el valor de la altura: "))
        res = paralelogramo(lado, altura)
        print("La superficie del paralelogramo es: %.2f" % (res))
    
    elif opcion == 4 :
        print("FINALIZADO...")

    else :
        print("Opción inválida :)")

main()
    