#Sebastian Cortes Tellez A01709967
import math

def sector(radio,angulo):
    sec = ((math.pi * radio**2) * angulo) / 360
    return sec

def eclipse(a,b):
    ecl = math.pi * a * b
    return ecl

def paralelogramo(a,h):
    par = a * h
    return par

def superficies():
    print("1. Sector\n2. Eclipse\n3. Paralelogramo\n4. Salir")

def main():
    superficies()
    op = int(input("Eliga una opcion: "))
    if op==1:
        rad = float(input("Introduzca el radio: "))
        ang = float(input("Introduzca el angulo: "))
        res = sector(rad,ang)
        print("Resultado: %0.2f" % res)
    elif op==2:
        a = float(input("Introduzca el radio a: "))
        b = float(input("Introduzca el radio b: "))
        res = eclipse(a,b)
        print("Resultado: %0.2f" % res)
    elif op==3:
        a = float(input("Introduzca el lado: "))
        h = float(input("Introduzca la altura: "))
        res = paralelogramo(a,h)
        print("Resultado: %0.2f" % res)
    elif op==4:
        print("Adios")
    else:
        print("Opcion invalida")
        
main()