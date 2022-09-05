#Construye las funciones para calcular la superficie de cada una de las siguientes figuras
#Circulo
#Elipse
#Paralelogramo
import math 

def sector (radio, angulo):
    resul= (math.pi * radio**2) * angulo / 360
    return resul

def eclipse (ra, rb):
    resul = (math.pi * ra) * rb
    return resul

def paralelogramo (longitud, altura):
    resul = longitud * altura
    return resul

def  superficies ():
    print(" 1. Sector")
    print(" 2. Eclipse")
    print(" 3. Paralelogramo")
    print(" 4. Salir")

def main ():
    superficies()
    opcion= int(input("Dame una opción para el menú: "))
    
    if opcion==1:
        radio= float(input("Ingresa un radio: " ))
        angulo= float(input("Ingresa un angulo: " ))
        resul= sector(radio, angulo)
        print("La superficie del sector es: %.2f" % (resul))
    
    if opcion==2:
        ra= float(input("Ingresa un primer radio: " ))
        rb= float(input("Ingresa un segundo radio: " ))
        resul= eclipse (ra, rb)
        print("La superficie de la elipce es: %.2f" % (resul))
    
    if opcion==3:
        longitud= float(input("Ingresa una longitud: " ))
        altura= float(input("Ingresa una altura: " ))
        resul= paralelogramo (longitud, altura)
        print("La superficie del paralelogramo es: %.2f" % (resul))
    
    elif opcion==4:
        print("Adiós :D")
     
    else:
        print(" Opción invalida")

main ()


