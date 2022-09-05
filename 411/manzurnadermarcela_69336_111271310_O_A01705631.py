# Marcela Manzur Nader (A01705631)


import math

def sector(radio, angulo):
    S = ( math.pi *radio**2*angulo) / 360
    return S

def eclipse (a,b):
    S = (math.pi*a*b)
    return S

def paralelogramo(La,Lh):
    S = (La*Lh)
    return S

def superficie():
    print("1.sector \n2. Eclipse \n3.paralelogramo \n4. Salir")

def main():
    superficie()
    opcion = int(input("Dame una opcion"))
    if opcion == 1:
        radio  = float(input("dame el radio:"))
        angulo = float(input("dame el angulo:"))
        S = sector(radio,angulo)
        
        print("La superficie es: %.2f " % sector(radio, angulo))
    elif opcion == 2:
        a  = float(input("dame el valor de a:"))
        b = float(input("dame el valor de b:"))
        S = eclipse(a,b)
       
        print("La superficie es: %.2f" % eclipse(a,b))
    elif opcion == 3:
        La = float(input("dame el valor de La:"))
        Lh = float(input("dame el valor de Lh:"))
        S = paralelogramo(La,Lh)
        
        print("La superficie es: %.2f " % paralelogramo(La,Lh))
    elif opcion == 4: 
        print("adios")
    else:
        ("opcion invalida")
main()
         
        