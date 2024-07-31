"""Joao Pedro Correia"""
import os

opcao='s'
while opcao == 's':
    os.system("cls")
    print("Ex 1 - Tabuada\nEx 2 - Vogais\n0 - Sair")
    case=int(input("Escolha: "))
    match case:
        case 0:
            break
        case 1:
            os.system("cls")
            numero=int(input("Escolha um número: "))
            print("Tabuada:")
            for i in range (1,11,1):
                print(f"{numero} x {i} = {numero*i}")
            
        case 2:
            os.system("cls")
            print("(favor  usar somente caracteres minusculos)")
            caracter1 = str(input("Digite o primeiro caracter: "))
            caracter2 = str(input("Digite o segundo caracter: "))
            caracter3 = str(input("Digite o terceiro caracter: "))
            caracter4 = str(input("Digite o querto caracter: "))
            caracter5 = str(input("Digite o quinto caracter: "))
            a=0
            if caracter1 == 'a' or caracter1 == 'e' or caracter1 == 'i' or caracter1 == 'o' or caracter1 == 'u':
                a=a+1
            if caracter2 == 'a' or caracter2 == 'e' or caracter2 == 'i' or caracter2 == 'o' or caracter2 == 'u':
                a=a+1
            if caracter3 == 'a' or caracter3 == 'e' or caracter3 == 'i' or caracter3 == 'o' or caracter3 == 'u':
                a=a+1
            if caracter4 == 'a' or caracter4 == 'e' or caracter4 == 'i' or caracter4 == 'o' or caracter4 == 'u':
                a=a+1
            if caracter5 == 'a' or caracter5 == 'e' or caracter5 == 'i' or caracter5 == 'o' or caracter5 == 'u':
                a=a+1
            print(f"{a} vogais")

        case _:
            print("Opção inválida")
    opcao=str(input("Deseja repetir?(s/n)\n"))
        