import os


count = 's'
while count == 's':
    os.system("cls")
    altura = float(input("Qual dua altura?\n"))
    sexo = int(input("""Qual seu sexo?
1:feminino
2:masculino\n"""))
    if sexo == 1:
        pesoideal = (62.1 * altura)-44.7
        print(f"Seu peso ideal é {pesoideal}")
    elif sexo == 2:
        pesoideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é {pesoideal}")

    count = str(input("Deseja repetir? (s/n)"))