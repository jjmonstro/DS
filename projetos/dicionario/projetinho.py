import os 
from subalgoritimos import *

#Joao Pedro Correia
#Matheus Bernardino Gomes

notas = {'Joao': 9.5,
         'Marina': 9.5,
         'Andre': 9.5}

while True:
    os.system("cls")
    print("""    0- Sair
    1- Adicionar novo Aluno | Nota (limite 10 alunos)
    2- Editar Aluno
    3- Listar os Alunos
    4- Excluir um Aluno
    5- Calcular (e exibir) a média da turma
    6- Consultar um aluno
    7- Apagar todos os alunos da sala""")
    opcao = input("Escolha: ")
    try:
        opcao=int(opcao)
    except:
        os.system("cls")
        input("""--Opção Inválida--
Aperte enter para continuar...""")
        continue
    match opcao:
        case 0:
            print("Saindo...")
            break
        case 1:
            os.system("cls")
            cadastrar_aluno(notas)
            input("Aperte enter para continuar...")
        case 2:
            os.system("cls")
            editar_aluno(notas)
            input("Aperte enter para continuar...")
        case 3:
            os.system("cls")
            listar_alunos(notas)
            input("Aperte enter para continuar...")
        case 4:
            os.system("cls")
            excluir_aluno(notas)
            input("Aperte enter para continuar...")
        case 5:
            os.system("cls")
            media_turma(notas)
            input("Aperte enter para continuar...")
        case 6:
            os.system("cls")
            consultar_aluno(notas)
            input("Aperte enter para continuar...")
        case 7:
            os.system("cls")
            apagar_sala(notas)
            input("Aperte enter para continuar...")
        case _:
            input("--Opção Inválida--\nAperte enter para continuar...")