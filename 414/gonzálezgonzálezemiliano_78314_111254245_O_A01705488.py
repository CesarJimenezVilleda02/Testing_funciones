#Emiliano González González A01705488
import math
def sector(radio, angulo):
    res=(math.pi * radio ** 2 * angulo)/360
    return res
def eclipse(a, b):
    res=math.pi * a * b
    return res
def paralelogramo(a, h):
    res=a * h
    return res
def superficies():
    print("1.Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
def main():
    superficies()
    opcion=int(input("Dame una opción:"))
    if opcion==1:
        a=float(input("Introduce el valor del ángulo:"))
        r=float(input("Introduce el valor del radio:"))
        sec=sector(a, r)
        print("El valor de la superficie es= %.2f" %(sec))
    elif opcion==2:
        a=float(input("Introduce el valor de a:"))
        b=float(input("Introduce el valor de b:"))
        sup=eclipse(a,b)
        print("El valor de la superficie es=%.2f" %(sup))
    elif opcion==3:
        a=float(input("Introduce el valor de a:"))
        h=float(input("Introduce el valor de h:"))
        sup=paralelogramo(a, h)
        print("El valor de la superficie es=%.2f" %(sup))
    elif opcion==4:
        print("Adios")
    else:
        print("Opción no válida")
main()
        
        
    