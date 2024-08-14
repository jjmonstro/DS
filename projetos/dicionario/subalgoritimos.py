import os
os.system("cls")

def cadastrar_aluno(d: dict):
    alunonovo = input("Digite o nome do aluno: ")
    while True:
        notaaluno = input("Insira a nota: ")
        if not notaaluno.isdecimal:
            print("Opção inválida!\nDigite um valor numerico") 
            
            continue
        notaaluno = float(notaaluno)
        if notaaluno > 10 or notaaluno<0:
            os.system("cls")
            input("------- Apenas notas até 10------")
            os.system("cls")
            continue
        else:
            break
    d[alunonovo] = notaaluno
    print("Aluno adicionado")

    # print(f'{alunonovo}') 
    # print(f'{notaaluno}')
    # print(d)

    def aluno_existe():
        ...
    
    

    