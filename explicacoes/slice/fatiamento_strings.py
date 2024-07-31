import os
os.system("cls")
#        01234567890123456789012345678901234567890123
frase = "Dia 29, acontecerá algo especial no planeta!"

print(frase)
print(frase[::-2])
# todos os exemplos de fatiamento de lista que usamos servem para strings

for i in range(len(frase)):
    print(frase[i], end = "")

print()

for i in range(0, len(frase), 2):
    print(frase[i], end = " ")

print()

for i in range(10, len(frase) -5, 1):
    print(frase[i], end = "")

print()

for carac in frase:
    print(carac, end="")
