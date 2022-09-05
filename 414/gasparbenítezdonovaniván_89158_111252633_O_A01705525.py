#A01705525 Donovan Iván Gaspar Benítez
import math
def sector(radio, angulo):
    res = (math.pi * radio ** 2 * angulo) / 360
    return res
def eclipse(a,b):
    res = math.pi * a * b
    return res
def paralelogramo(a,h):
    res = a * h
    return res
def superficies():
    print("1. Sector Circulo")
    print("2. Superficie Eclipse")
    print("3. Superficie Paralelogramo ")
    print("4. Salir")
    
def main():
    superficies()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        r = float(input("Dame el radio: "))
        a = float(input("Dame el angulo: "))
        res = sector(r,a) 
        print("%.2f" %(res))
    elif opcion == 2:
        ra = float(input("Dame el radio a: "))
        rb= float(input("Dame el radio b: "))
        res = eclipse(ra,rb)
        print("%.2f"%(res))
    elif opcion == 3:
        lon = float(input("Escribe la longitud: "))
        alt = float(input("Escribe la altura: "))
        res = paralelogramo(lon,alt)
        print("%.2f"%(res))
    elif opcion == 4:
        print("Adios")
    else:
        print("Opcion_Invalida")
main()    
