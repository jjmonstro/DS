import os

# Operador TERNÁRIO - Substitiu o if composto (com o else) em situações onde há somente um 
# comando do lado verdadeiro e um do lado false.
'''
Sintaxe:
[<var> = ] <comando True> if <condição> else <comando False>
'''
# Exemplo 1 (sem variável): Verificar se é maior de idade.
idade = 40
print("Menor de idade") if idade <= 18 else print("Maior de idade")

# Exemplo 2: utilizando comandos do SO
# dir lista arquivos e diretorios no windows
# ls lista arquivos e diretorios no Linux e Macos
os.system("cls" if os.name == "nt" else "clear")

# Exemplo 3 (com variável): Aplicando bonus
venda = 500
bonus = 50 if venda > 1000 else 30
print(venda, bonus)

# Exemplo 4 (parte do cálculo): Aplicando desconto em uma venda
venda = 7000
com_desconto = venda - (venda * 0.1 if venda > 1000 else venda * 0.05)
print(venda, com_desconto)