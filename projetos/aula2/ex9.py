import os
os.system("cls")
import math

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"O maior dos numeros é {num1}")
if num2 > num1 and num2 > num3:
    print(f"O maior dos numeros é {num2}")
if num3 > num1 and num3 > num2:
    print(f"O maior dos numeros é {num3}")

