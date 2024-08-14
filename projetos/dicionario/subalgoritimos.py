import os
os.system("cls")

#o dict está aqui para testes
# notas = {'Joao': 9.5,
#          'Marina': 3.6,
#          'Andre': 0.9}

def cadastrar_aluno(d: dict):
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
              
    d[nome] = nota
    print("Aluno adicionado")

    # prints para teste
    # print(f'{alunonovo}') 
    # print(f'{nota}')
    print(d)


def aluno_existe():
        ...
    
def nota_valida(s: str) -> bool:
     #ainda esta quebrando com .  ou 3..  

     #esse a é para resolver o problema 3..
     a=0
     for i in s:
         if not i.isnumeric():
             if i == '.':
                 a+=1
                 if a > 1:
                      print("--Nota Inválida--")
                      return False
                 continue
             else:
                 print("--Nota Inválida--")
                 return False
     s = float(s)
     if s > 10 or s < 0:
        print("--Nota Inválida--")
        return False
     else:
          return True

def nome_valido(n: str, d: dict) -> bool:
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



