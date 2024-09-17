#Joao Pedro Correia
#Matheus Bernardino Gomes
import os
# os.system("cls")

#o dict está aqui para testes
# notas = {'Joao': 9.5,
#          'Marina': 3.6,
#          'Andre': 0.9}

#----------------------------------------------
def cadastrar_aluno(d: dict) -> None:
    #Verificando o limite de 10
     if len(d.keys()) > 10:
          print("--Máximo de 10 alunos atingido--")
          return

    #Recebendo e verificando nome
     while True:
         nome = input("Digite o nome do aluno: ")
         if not nome_valido(nome,d):
              continue
         else:
              break
    #Recebendo e verificando nota
     while True:
         nota=input("Insira a nota do aluno: ")
         if not nota_valida(nota):
              continue
         else:
              nota=float(nota)
              break
              
     d[nome.capitalize()] = round(nota,1)
     print("Aluno adicionado!!")

    # prints para TESTE
    # print(f'{alunonovo}') 
    # print(f'{nota}')
    # print(d)
    
#----------------------------------------------
def nota_valida(s: str) -> bool:
     #isso era antes de TRY EXCEPT
     # if s.count('.')>1 or s=='':
     #      print("--Nota Inválida--")
     #      return False 
     # for i in s:
     #     if not i.isnumeric():
     #         if i == '.':
     #             continue
     #         else:
     #             print("--Nota Inválida--")
     #             return False
     # s = float(s)
     # if s > 10 or s < 0:
     #    print("--Nota Inválida--")
     #    return False
     # else:
     #      return True
     
     try:
        s = float(s)
     except ValueError:
          print("--Nota Inválida--")
          return False
     else:
          if s > 10 or s < 0:
               print("--Nota Inválida--")
               return False
          else:
               return True
#----------------------------------------------
def nome_valido(n: str, d: dict) -> bool:
     if n == '':
          print("--Nome Inválido--")
          return False
     n=n.capitalize()
     schar='!@#$%¨&*()_+=-/¬¢£.,><;:][}{?\|\'\"][ªº°'
     for i in n:
          if i.isnumeric() or i in schar:
               print("--Nome Inválido--")
               return False
     if d.get(n):
         print("--Nome já existente--")
         return False
     else:
          return True

#----------------------------------------------
def listar_alunos(d: dict)  -> None:
     print("  Nome           Nota")
     pontos='................' #10 pontos
     for k, v in d.items():
          #se tiver 17 caracteres ou mais ele buga a exibição
          qpontos = len(pontos) - len(k)
          print(f"  {k}{pontos[:qpontos:]}{v}")

#----------------------------------------------
def editar_aluno(d: dict)  -> None:
     #Recebendo e verificando se nome existe
     while True:
         nome = input("Digite o nome do aluno: ")
         nome = nome.capitalize()
         if d.get(nome.capitalize()):
              break
         else:
              print("--Aluno não existe--")
              input("Aperte enter para continuar...")
              continue
     
     #recebendo e verificando nota
     while True:
         nota=input("Insira a nova nota do aluno: ")
         if not nota_valida(nota):
              continue
         else:
              nota=float(nota)
              break
     print("Aluno Editado com sucesso!!")
     d.update([(nome,nota)])

#----------------------------------------------
def excluir_aluno(d: dict)  -> None:
     #Recebendo e verificando se nome existe
     while True:
         nome = input("Digite o nome do aluno: ")
         nome = nome.capitalize()
         if d.get(nome.capitalize()):
              break
         else:
              print("--Aluno não existe--")
              input("Aperte enter para continuar...")
              continue
         
     d.pop(nome)
     print("Aluno deletado com sucesso!!")

#----------------------------------------------
def media_turma(d:dict)  -> None:
     a=0
     soma=0
     for v in d.values():
          soma=v+soma
          a+=1

     print(f"A média da turma é: {soma/a}")

#----------------------------------------------
def consultar_aluno(d: dict)  -> None:
     while True:
         nome = input("Digite o nome do aluno que deseja consultar: ")
         nome = nome.capitalize()
         if d.get(nome.capitalize()):
              break
         else:
              print("--Aluno não existe--")
              input("Aperte enter para continuar...")
              continue
     print("  Nome           Nota")
     pontos='................' #10 pontos
     #se tiver 17 caracteres ou mais ele buga a exibição
     qpontos = len(pontos) - len(nome)
     os.system("cls")
     print("  Nome           Nota")
     print(f"  {nome}{pontos[:qpontos:]}{d[nome]}")
     

#----------------------------------------------
def apagar_sala(d:dict)  -> None:
     d.clear() 
     print("Todos os dados foram apagados com sucesso!!")
     