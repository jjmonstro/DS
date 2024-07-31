import os
os.system("cls")
#        01234567890123456789012345678901234567890123
frase = "Dia 29, acontecerá algo especial no planeta!"

# Método find => procura uma substring em uma string, se encontrar retorna o indice, senao -1
"""
print(frase.find("algo"))
print(frase.find(","))
print(frase.find("a"))
print(frase.find("a",3))
print(frase.find("a",9, 25))
print(frase.find("z"))

if frase.find("a") == -1:
    print("nao existe")
else:
    print("existe")
"""

# Método join() => transforma uma lista de string em apenas uma string

lista_str = ["Edson", "de", "Oliveira"]
print(lista_str, len(lista_str))
print(" ".join(lista_str), len(" ".join(lista_str)))


# Método split() => contrário do join
"""
nome = "Edson de Oliveira"
print(nome)
print(nome.split())
print(nome.split("e"))
print(nome.split("de"))
print(nome.split("z"))
"""

# Método replace() => substitui um trecho por outro
#        01234567890123456789012345678901234567890123
"""
frase = "Dia 29, acontecerá algo especial no planeta!"
nome = "Edson de Oliveira da silva nogueira"
nome_new1 = nome.replace('e', 'E')
print(nome_new1)
nome_new2 = nome.replace('de', 'DE')
print(nome_new2)
nome_new3 = nome.replace('e', 'caramba que coisa incrivel')
print(nome_new3)
nome_new4 = nome.replace(' ', '_')
print(nome_new4)
nome_new5 = nome.replace(' ', '_', 2)
print(nome_new5)
"""

# Método strip() => Elimina os espaços anteriores e posteriores da string
"""
texto = "Gostei produto estou usando strip chegou atrasado gostei"
print(texto)
print (texto.strip())
"""

# operador de identidade
"""num = 3
lista_num = [1, 2, 3, 4, 5, 6, 7, 8]
if num in lista_num:
    print("Achou")
else:
    print("nao achou")

nome = "Maria da silva."

if "." not in nome:
    nome = nome + "."


print(nome)"""