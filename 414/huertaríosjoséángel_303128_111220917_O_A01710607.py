#Jose Angel Huerta Rios A01710607

import math

def sector (radio, angulo):
    res = (math.pi * (radio ** 2) * angulo) / 360
    return res

def eclipse (a, b):
    s = math.pi * a * b
    return s

def paralelogramo (a, h):
    s = a * h
    return s
def superficies():
    print('1. Sector')
    print('2. Eclipse')
    print('3. Paralelogramo')
    print('4. Salir')

def main():
    superficies()
    opcion = int(input('Elije una opcion: '))
    
    if opcion == 1:
        r = float(input('Introduce el radio: '))
        a = float(input('Introduce el angulo: '))
        res = sector(r, a)
        print('La superficie de la figura es %.2f' % (res))
        
    elif opcion == 2:
        a = float(input('Introduce el radio a: '))
        b = float(input('Introduce el radio b: '))
        res = eclipse(a, b)
        print('La superficie de la figura es %.2f' % (res))
        
    elif opcion == 3:
        a = float(input('Introduce el lado a: '))
        b = float(input('Introduce la altura h: '))
        res = paralelogramo(a, b)
        print('La superficie de la figura es %.2f' % (res))
        
    elif opcion == 4:
        print('Bye')
        
    else:
        print('Opcion no valida')
main()
