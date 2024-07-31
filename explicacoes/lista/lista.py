import os
os.system("cls")

# l = ["Correia",12,1.67,True,34]
# print(l[1])
# print(f"{l}\n")

# l[4]="Correx"
# print(l)

#append adiciona um item na lista, logo após o último
lista = list()
print(lista)
lista.append(22)
lista.append("João")
print(lista)

#insert insere um elemento em um indíce específico
lista.insert(1,57.7)
print(lista)

#pop remove um elemento, por defalt ele tira o último mas pode especificar o ínícÊ
lista.pop(0)
print(lista)

#remove remove o elemento pelo conteúdo, não pelo indicé (se seu conteu espcificado não existir quebra)
lista.remove(57.7)
print(lista)

#index retor o indice do elemento passado por parâmetro, se não  tiver esse indice, ele quebra 
indice=lista.index("João")
print(f"indice = {indice}")

#count retorna a quantos elementos da lista são iguais ao do parâmetro
#se não tiver nenhum elemento igual ao especificado retorna 0
qtd = lista.count("João")
print(qtd) 

#len retorna quantos elementos tem na lista
lista.append(22)
lista.append(57.7)
qtd = len(lista)
print(qtd) 

#sum retorna a soma os elemntos da lista se forem numericos, se não forem todos numricos ele quebra
#print(sum(lista))

# + concatena listas
lista1=[1,2,3]
lista2=[4,5,6]
lista3= lista1 + lista2
print(lista1)
print(lista2)
print(lista3)

lista2=lista1+lista2
print(lista2)

lista3=lista2+lista1
print(lista3)

#extend adiciona ao final da lista outra lisa
lista2=[4,5,6]

lista2.extend(lista1)
print(lista2)

#copy copia uma lista em outra
# lista2.copy(lista)
# print(lista2)

#sort ordena os elementos da lista
lista = [19,4,25,33,-5,-12,0]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#reverse reverte a ordem, primeira vai pra ultimo e blá blá blá
lista4=lista2.reverse()
print("\nreverse")
print(lista4)

#clear limpa a lista
lista2.clear
print(lista2)

#del deleta a lista
del(lista2)