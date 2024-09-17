import os

"""to do
poder sair do editar
procedimento de verificar se ey existe"""

dicionario = {
    "Nome" : "Matheus",
    "Idade" : 17,
    "Casado" : True
}

#Subalgoritimos


#esse é o antigo preencher
def addItem(d: dict) -> None:
    while True:
        os.system("cls")
        key = input("Insira uma nova key: ")
        if d.get(key):
            input("Essa key já existe\nAperte enter para seguir...")
            continue
        else:
            break
    value = input("Insira o value: ")
    d.update([(key,value)])
    input("Dicionário atualizado com sucesso!!\nAperte enter para seguir...")

def exibir(d: dict) -> None:
    pontos='...........'
    print(f"Key........Value")
    for k,v in d.items():
        qpontos = len(pontos) - len(k)
        print(f"{k}{pontos[:qpontos:]}{v}")
        
def editar(d: dict) ->  None:
    while True:
        os.system("cls")
        print("Estado atual:")
        exibir(d)
        while True:
            key = input("Insira a key que deseja editar(0-sair): ")
            if key == '0':
                return 0
            if not d.get(key):
                print("Essa key não existe, tente novamente()")
                continue
            else:
                break
          
        value = input("Insira o novo value: ")
        d.update([(key,value)])
        input("Dicionário atualizado com sucesso!!\nAperte enter para seguir...")
        break

def addKey(d: dict) -> None:
    print("Estado atual:")
    exibir(d)
    while True:
        key = input("Insira uma nova key: ")
        if d.get(key):
            input("Essa key já existe\nAperte enter para seguir...")
            continue
        else:
            break
    d.update([(key, None)])
    input("Dicionário atualizado com sucesso!!\nAperte enter para seguir...")

def excluir(d: dict) -> None:
    print("Estado atual:")
    exibir(d)
    while True:
        key = input("Insira a key que deseja excluir(0-sair): ")
        if key == '0':
            return 0
        if not d.get(key):
            print("Essa key não existe, tente novamente")
            continue
        else:
            break
    d.pop(key)
    input("Dicionário atualizado com sucesso!!\nAperte enter para seguir...")

def clear(d: dict) -> None:
    d.clear()
    input("Dicionário limpo com sucesso!!\nAperte enter para seguir...")

#---------------------------------------------------------------------------------
while True:
    os.system("cls")
    print("""    0- Sair
    1- Preencher Dicionario 
    2- Exibir dicionario | dado a dado
    3- Editar dicionario | exibir estado anterior
    4- Criar nova key
    5- Excluir key
    6- Excluir todas as keys""")
    escolha = input("Escolha: ")
    try:
        escolha = int(escolha)
    except:
        input("Escolha invalida demais!!!!\nAperte enter para seguir...")
        continue
        
    match escolha:
        case 0:
            os.system("cls")
            print("Obrigado por testar o sistema!")
            break
        case 1:
            os.system("cls")
            addItem(dicionario)
        case 2:
            os.system("cls")
            exibir(dicionario)
            input("Aperte enter para seguir...")
        case 3:
            os.system("cls")
            editar(dicionario)
        case 4:
            os.system("cls")
            addKey(dicionario)
        case 5:
            os.system("cls")
            excluir(dicionario)
        case 6:
            os.system("cls")
            clear(dicionario)
        case _:
            input("""Opção inválida\nAperte enter para seguir...""")
            continue


