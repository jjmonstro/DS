import os
os.system("cls")
"""
ideia
1. transfar o arq sujo em uma lista com cada linha
2. transformar essa lista em uma string gigantesca
3. transformar essa string em uma lista com cada palavra
4. verificar se os itens dessa lista correspondem a algun iten das palvras inuteis, se sim, tira esse item da lista
Pronto!!! você tera uma lista com as palavras pertinentes,
é só colocar no arquivo com writelines e contar qual item mais se repete
"""


#isso aqui seria para preencher o sujo.txt
# with open("sujo.txt", "w+", encoding="utf-8") as arq:
#     lista=[]
#     while True:
#         linha=input("Linha: ")
#         if linha!="":
#             lista.append(linha+"\n")
#         else:
#             break
#     arq.writelines(lista)


listaComentarios = [
    #                                        | esse 'em' não sai e eu não sei porque
    "em e Ótimo Ótimo Ótimo Ótimo Ótimo Ótimo Ótimo Ótimo produto! em Chegou rápido e em perfeito estado.\n",
    "Excelente custo-benefício. Recomendo a todos.\n",
    "Muito satisfeito. Funciona perfeitamente.\n",
    "Entrega rápida. Produto conforme descrito.\n",
    "Adorei! Superou minhas expectativas.\n",
    "Bom desempenho. Valeu cada centavo.\n",
    "Produto de qualidade. Atendeu todas as minhas necessidades.\n",
    "Recomendo. Ótima compra\n.",
    "Muito bom. Chegou antes do prazo.\n",
    "Perfeito. Exatamente como na descrição.\n",
    "Excelente. Funciona muito bem.\n",
    "Produto top. Muito satisfeito com a compra.\n",
    "Ótima compra. Voltaria a comprar.\n",
    "Muito bom. Recomendo a todos.\n",
    "Produto excelente. Chegou rápido e bem embalado.\n",
    "Adorei. Superou minhas expectativas.\n",
    "Muito satisfeito. Produto de qualidade.\n",
    "Entrega rápida. Produto conforme descrito.\n",
    "Ótimo custo-benefício. Recomendo.\n",
    "Produto excelente. Funciona perfeitamente."
] 

palavrasDescartaveis=["e", "em", "do", "a", "na", "as", "de"]

with open("sujo.txt", "w+", encoding="utf-8") as arq:
    arq.writelines(listaComentarios)



with open("sujo.txt", "r+", encoding="utf-8") as arqs, open("limpo.txt", "w+", encoding="utf-8") as arql:
    listaSujo=arqs.readlines()

    stringSujo=" ".join(listaSujo)

    listaPalavras=stringSujo.split()

    listaPalavrasLower=[]
    for i in listaPalavras:
        i = i.lower().rstrip('.')
        listaPalavrasLower.append(i)

    listaFiltrada=[]
    for i in listaPalavrasLower:
        if i not in palavrasDescartaveis:
            listaFiltrada.append(i+"\n")
    
    itemMaisRepete=0
    maiorRept=0

    for item in listaFiltrada:
        contagem=0
        for i in listaFiltrada:
            if i == item:
                contagem+=1
        if contagem>maiorRept:
            maiorRept=contagem
            itemMaisRepete=item
    arql.writelines(listaFiltrada)
    print("A palavra que mais se repete é: "+itemMaisRepete)
    
    

