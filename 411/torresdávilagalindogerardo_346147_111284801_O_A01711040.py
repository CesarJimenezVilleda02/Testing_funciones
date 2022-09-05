#Gerardo Torres Davila funciop sector

import math
angulo = float(input("Dame un angulo del circulo"))
radio = float(input("Dame el radio del circulo"))
sector = ((math.pi)*(radio**2)*angulo)/360


ladoA = float(input("Dame un lado del elipse"))
ladoB = float(input("Dame un lado del elipse"))
elipse = math.pi * ladoA * ladoA


lado = float (input("Dame un lado del paralelogramo"))
h = float(input("Dame la altura del paralelogramo"))
paralelogramo = lado * h

print ("1. El sector es:", sector)
print ("2. El elipse es:", elipse)
print ("3. El paralelogramo es:", paralelogramo)
print ("4. Salir")