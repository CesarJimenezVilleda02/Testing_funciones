# Santiago Garcia Fernandez (A01705091)
import math

def sector(r, a):
    r = radio
    a = angulo
    res = (maht.pi * radio**2 * a) / 360
    return res

def elipse(a, b):
    r1 = radio1 
    r2 = radio2
    res = (math.pi * a * b)
    return res

def paralelogramo(a, h):
    a = lado
    h = altura
    res = (a * h)
    return res

def superficies():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
def main():
    superficies()
    opcion = int(input("Dame una opcion: "))
    if opcion == 1:
        r = float(input("Dame el sector: "))
        res = sector(r, a)
        print("Sector = %.1f" % (r, res))
    elif opcion == 2:
        r = float(input("Dame el elipse: "))
        res = elipse(ra, rb)
        print("Elipse = %.1f" % (r, res))
    elif opcion == 3:
        r = float(input("Dame el paralelogramo: "))
        res = paralelogramo(a, h)
        print("Paralelogramo = %.1f" % (r, res))
    elif opcion == 4:
        print("Hay nos vemos")
    else:
        print("Opcion invalida")

main()

                  
        
        
