import os
os.system("cls")


# Trabalhando com índices negativos

#         0   1   2   3   4   5   6   7   8   <== índices positivos
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#        -9  -8  -7  -6  -5  -4  -3  -2  -1   <== índices negativos

print(lista)
print(lista[0])
print(lista[-1])

# Fatiamento de listas

nova_lista = lista[2: 7]
print(nova_lista)
print(lista[-6: -3])

# lista[inicio: fim - 1: passo]
print(lista[-6: -3: 1])
print(lista[-8: -1: 2])
print(lista[8: 0: -2])
print(lista[::-1])
