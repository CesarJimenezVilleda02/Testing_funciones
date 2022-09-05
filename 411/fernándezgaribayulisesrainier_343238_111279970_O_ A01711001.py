# Ulises Rainier Fernandez Garibay A01711001

import math
def sector (r,a):
    res = (math.pi * (r*r) *a)/ 360
    retur = res
    
def elipse (a,b):
    r = math.pi * a * b
    return r

def paralelogramo  (b,h):
    R = b * h 
    return R

def areas ():
    print ("1.Area del sector del Circulo")
    print("2.Area del Elipse")
    print("3.Area del Paralelogramo")
    print("4.Salir")
    
def main():
    areas()
    opcion =float (input( "Dame una opcion:"))
    
    if opcion == 1:
        r = float (input( "dame el radio:"))
        a = float (input( "dame el angulo:"))
        print("sector(%.1f)= %.2f" % (r,a))
        
    elif opcion == 2:
        a = float (input( "dame el radio a:"))
        b = float (input( "dame el radio b:"))
        print("elipse(%.1f)= %.2f" % (a,b))
        
    elif opcion == 3:
        b = float (input( "dame el  lado:"))
        h = float (input( "dame la haltura:"))
        print("paralelogramo(%.1f)= %.2f" % (b,h))
        
    elif opcion == 4:
        print("adios")
        
    else:
        print ("opcion invalida, intente de nuevo")
        
main()
        
    
        
    

