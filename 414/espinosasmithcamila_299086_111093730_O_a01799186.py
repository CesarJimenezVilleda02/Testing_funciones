#Camila Espinosa Smith (a01799186)

import math

def sector(radio, angulo):
    res = (math.pi * radio**2 * angulo) / 360
    return res

def elipse (a, b):
    res = math.pi * a * b
    return res

def paralelogramo ( a, h):
    res= a * h
    return res

def superficies ():
    print("1. Sector")
    print("2. Eclipse")
    print("3. Paralelogramo")
    print("4. Salir")
    
def main ():
    superficies ()
    opcion = int( input( "Dame una opción:"))
    if opcion == 1:
        r = float( input( "Dame el radio:"))
        a = float( input ("Dame el angulo"))
        res = sector(r, a)
        print( "El área del sector de un circulo con radio de %.2f y un angulo de %.2f = %.2f" % (r, a, res))
    elif opcion == 2:
        a = float( input( "Dame a:"))
        b = float( input ("Dame b:"))
        res = elipse (a, b)
        print( "El área de la elipse es = %.2f" % res)
    elif opcion == 3:
        a = float( input( "Dame a:"))
        h = float( input ("Dame h:"))
        res = paralelogramo ( a, h)
        print( "El área de paralelogramo es = %.2f" % res)
    elif opcion == 4:
        print ("Adiós.")
    else:
        print("opción inválida.")
        
main()
    