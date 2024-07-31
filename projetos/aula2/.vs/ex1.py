import os
os.system("cls")

valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))

if valor1 > valor2:
    print(f"{valor1} é o maior")
elif valor2 > valor1:
    print(f"{valor2} é o maior")
else:
    print("Os valores devem ser diferentes")


