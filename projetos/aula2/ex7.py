import os
os.system("cls")
import math

count = 's'
while count == 's':
    lados=int(input("Número de lados: "))
    medidaLados=float(input("Medida(cm) dos lados: "))

    if lados == 3:
        area=(medidaLados*medidaLados)/2
        print(f"TRIÂNGULO, área = {area}")
    elif lados==4:
        area=medidaLados^2
        print(f"QUADRADO, área = {area}")
    elif lados==5:
        print("PENTÁGONO")
    else:
        print("erro")
    

    count = str(input("Deseja repetir? (s/n)"))