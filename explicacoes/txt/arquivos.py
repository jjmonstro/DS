# Manipulação de arquivos
'''
Modo de abertura:
----------------
'w' | write - gravar
'r' | read - ler
'a' | append - Edição de arquivo
'x' | gravação em arquivo exclusivo
'+' | gravar e ler ao mesmo tempo

função open() -> abre um arquivo
--------------------------------
Sintaxe:
    <obj> = open("Nome_arquivo", "modo_abertura")
'''
import os
os.system("cls")

# Abrindo um arquivo e gravando
"""
arq = open("arq1.txt", "w", encoding= "utf-8")
arq.write("Nossa que legal, gravou!\n") # write grava uma linha no arquivo
arq.write("de novo, de novo!\n")
arq.write("Gravação!")

arq.close()
"""
# Lendo um arquivo
"""
try:
    arq = open("arq1.txt", "r", encoding= "utf-8")
    print(arq.read()) # Lê o arquivo integralmente
    arq.close()
except FileNotFoundError:
    print("Arquivo não existe")
""" 

arq = open("arq1.txt", "a", encoding= "utf-8")
arq.write("\nnova linha!")
arq.close()

arq = open("arq2.txt", "w+", encoding= "utf-8")
arq.write("nova linha!")
arq.seek(2) # posiciona o cursor no arquivo texto
print(arq.read())
arq.close()

caminho = "d:\\aula\\arquivo\\"
caminho += "arq1.txt"
# Operador de contexto - with
with open(caminho,"r", encoding="utf-8") as arq:
    print(arq.read())
    dfgdfsgfd
    sdfgdfsgdsf
    sdfgsdfgdfs
sadfsad
sadfsdafsda
asdfdsa

"""
Exercicio:

Crie um menu que permita ao usuario
manipular um arquivo com os modos de abertura apresentados (exceto o +)
"""



