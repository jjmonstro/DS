#não faço idéia do erro, deve ser algo profundo do python
import os

while True:
    os.system ("cls")
    print("""1-Editar frase
2-Organizar lista
3-Preencher lista""")
    escolha = int(input("Qual exercício você deseja? (0 sair)\n"))

    # if not escolha.isnumeric():
    #     input("Opção inválida!\nPressione alguma tecla para continuar . . .")
    #     continue

    match escolha:
        case 0:
            break
        case 1:
            frase = str(input("Escreva a frase: "))
            a=1
            while a==1:
                localizado = str(input("Caractere a ser localizado: "))
                if len(localizado) != 1:
                    input("deve ser só um caracter, enter para continuar...")
                    continue
                troca = str(input("Trocar pelo caractere: "))
                if len(troca) != 1:
                    input("deve ser só um caracter")
                    continue
                a=0
            new_frase = frase.replace(localizado,troca)
            print(frase)
            print(new_frase)
        case 2:
            l = [45,5.7,"Férias",True,False,99,34]
            l_int = []
            l_float = []
            l_str = []
            l_bool = []
            print(l)
            for i in range(len(l)):
                if type(l[i]) == int:
                    l_int.append(l[i])
                if type(l[i]) == float:
                    l_float.append(l[i])
                if type(l[i]) == str:
                    l_str.append(l[i])
                if type(l[i]) == bool:
                    l_bool.append(l[i])
            print(l_int)
            print(l_float)
            print(l_str)
            print(l_bool)
        case 3:
            l = []
            for i in range(10):
                l.append(input("Insira elementos na lista (limite 10)\n"))
            print(l)
        case _:
            input("inválido, enter para continuar...")
            continue
    input("Aperte enter para continuar...")