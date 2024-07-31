import os
os.system("cls")

def preenche_lista(l: list):
    l.append(22)
    l.append("Bolsonaro")
    # ou
    # l.append(input("Insira um valor"))
    # print(f"{l}\n")
    #dava para colocar opcao de inserir mais e tals mais bruh

def exibe_lista(l: list):
    print(l)

def conta_elementos(l: list) -> int:
    x=len(l)
    return x

def retorna_indice(l: list, elemento) -> int:
    #print(len(l))
    tamanho=len(l)
    #print(tamanho-1)
    for i in range(tamanho):
        #print(i)
        if elemento == l[i]:
            return i
        
    return -1
    
def busca(l: list, elemento) -> int:
    a=0
    for i in range(len(l)):
        if elemento == l[i]:
            a+=1
    return a

def conta_inteiro(l: list) -> int:
    a = 0
    for i in range(len(l)):
        if  type(l[i]) == float:
            a+=1
    return a



lista = [-5, 22, 36, 785, -54]

# preenche_lista(lista)
# exibe_lista(lista)
# conta_elementos(lista)
print(retorna_indice(lista,-54))
# busca()
# print(busca(lista,22))