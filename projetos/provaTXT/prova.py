#Joao Pedro Correia

#nome do arquivo -- Joao.txt

def tem_letra(l: str) -> bool:
    for i in l:
        try:
            i=int(i)
        except:
            return True
    return False

def tem_numero(l: str) -> bool:
    a=False
    for i in l:
        try:
            i=int(i)
            a=True
        except:
           continue
    return a

import os 
while True:
    print("""MENU

0 - SAIR
1 - Digite as credenciais (Login Senha)
2 - Exibir o Arquivo
    """)
    opcao = input("Escolha:")
    try:
        opcao=int(opcao)
    except:
        print("\nopção inválida!\n")
        continue
    match opcao:
        case 0:
            break
        case 1:
            os.system("cls")
            #login
            while True:
                login=input("Login: ")
                if len(login) != 6:
                    print("ERRO! Digite um login válido")
                    continue

                try:
                    a=int(login[0])
                except:
                    print("ERRO! Digite um login válido")
                    continue

                if tem_letra(login) == False:
                    print("ERRO! Digite um login válido")
                    continue
                else:
                    break

            #senha
            while True:
                senha=input("Senha: ")
                if len(senha) < 6:
                    print("ERRO! Digite uma senha válida")
                    continue

                try:
                    a=int(senha[0])
                    print("ERRO! Digite uma senha válida")
                    continue
                except:
                    if tem_numero(senha) == False:
                        print("ERRO! Digite uma senha válida")
                        continue 
                    else:
                        break
            with open("Joao.txt", "a+", encoding="utf-8") as arq:
                lista=[login+", ",senha+"\n"]
                print("LOGIN E SENHA GRAVADOS COM SUCESSO!")
                arq.writelines(lista)

        case 2:
            with open("Joao.txt", "r", encoding="utf-8") as arq:
                os.system("cls")
                print(arq.read())
                
        case _:
            input("Opção inválida\nEnter para continuar...")