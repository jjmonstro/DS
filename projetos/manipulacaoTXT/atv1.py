import os
os.system("cls")

# with open("arq.txt", "w+", encoding="utf-8") as arq:
#     arq.write("linha 1\n")
#     arq.write("linha 2\n")
#     arq.write("linha 3")
#     arq.seek(0)
#     # listaLinhas=arq.readlines()
#     # print(listaLinhas[2])
#     for linha in arq.readlines():
#         print(linha,end='')

# with open("arq.txt", "w+", encoding="utf-8") as arq:
#     print("\nGravando de linha em linha")
#     while True:
#         linha=input("Linha: ")
#         if linha!="":
#             arq.write(linha + '\n')
#         else:
#             break
#     print("\nExibindo...")
#     arq.seek(0)
#     print(arq.read())

with open("arq.txt", "w+", encoding="utf-8") as arq:
    lista=[]
    while True:
        linha=input("Linha: ")
        if linha!="":
            lista.append(linha+"\n")
        else:
            break
    arq.writelines(lista)
    arq.seek(0)
    os.system("cls")
    print(arq.read())
