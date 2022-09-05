#Ian Alejandro Melo Tolosa, A01742009
import math

def sector(radio, angulo):
    sector = (math.pi * radio ** 2 * angulo) / 360
    return sector

def eclipse(a,b):
    eclipse = math.pi * a * b
    return eclipse

def paralelogramo(a,h):
    paralelogramo = a*h
    return paralelogramo

def superficie():
    print("1.-Sector")
    print("2.-Eclipse")
    print("3.-Paralelogramo")
    
def main():
    superficie()
    opciones = int(input("Dame una opción:"))
    if opciones == 1:
        r = float(input("Dame el radio:"))
        a = float(input("Dame el angulo:"))
        valores = sector(r,a)
        print("Radio(%.2f) y Angulo(%.2f) dan como resultado un sector de %.2f" % (r,a,valores))
    
    elif opciones == 2:
        a = float(input("Dame el valor de a:"))
        b = float(input("Dame el valor de b:"))
        valores = eclipse(a,b)
        print("El radio a(%.2f) y el radio b(%.2f) dan como resultado una eclipse de %.2f" % (a,b,valores))
    
    elif opciones == 3:
        a = float(input("Dame el lado a:"))
        h = float(input("Dame la altura:"))
        valores = paralelogramo(a,h)
        print("El lado a(%.2f) y la altura(%.2f) dan como resultado un paralelogramo de %.2f" % (a,h,valores))

    elif opciones == 4:
        print("Adiós")
        
    else:
        print("Opción invalida")
                

main()
              