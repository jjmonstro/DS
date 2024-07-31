import os
from subalgoritimos import *


v = [45, -89, 32,-12, 33]
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

while True:
    os.system("cls")
    print(""" 
    0. S A I R
    1. Primeiro elemento do vetor. 
    2. Exiba somente os números negativos contidos no vetor.
    3. Soma dos elementos do vetor
    4. Média dos elementos do vetos
    5. Numeros ímpares contidos no vetor
    6. Exiba o primeiro e ultimo elemento do vetor
    7. Exiba elementos de índice par
    8. Verifica se o valor existe no vetor
    9. Ordena os elemtos do vetor
    10. Copia os elemtos de v1 em v2
    11. Copia os elemtos de v1 invertidos em v2
    12. Ordena o vetor de forma crescente
    13. Ordena o vetor de forma decrescente
    14. Ordena vetor de acordo com a escolha
    15. Ordena valores pares em ímpares
    16. Quantos valores estão acima da média
    17. Maior elemento do vetor
    """)
    opcao = input("Escolha: ")
    if not opcao.isnumeric():
        input("Opção inválida!\nPressione alguma tecla para continuar . . .")
        continue
    opcao = int(opcao)

    match opcao:
        case 0:
            break
        case 1:
            print(primeiroElemento(v))

        case 2:
            achaNega()

        case 3:
            print(somaVet(v))

        case 4:
            print(mediaVet(v))

        case 5:
            print(achaImpar(v))
        case 6:
            print(exiba_extremos(v))
        case 7:
            print(exibe_indice_par(v))
        case 8:
            print(existeOuNao(32))
        case 9:
            print(ordenaVetor(v))
        case 10:
            copiaVet(v1,v2)
        case 11:
            inverte_vetor(v1,v2)
        case 12:
            ordena_vetor_crescente(v1)
        case 13:
            ordena_vetor_decrescente(v1)
        case 14:
            ordena_vetor_geral(v1, 'c')
        case 15:
            separaParesImpares(v1)
        case 16:
            print(acima_media(v1))
        case 17:
            print(maior_elemento(v1))
        case _:
            ...
    input("Aperte qualquer tecla para continuar . . .")


