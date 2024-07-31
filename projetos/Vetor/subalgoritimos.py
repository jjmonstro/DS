v = [45, -89, 32,-12, 33]
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

#EXERCÍCIO 1
def primeiroElemento(v: list) -> int:
    x=v[0]
    return x

#EXERCÍCIO 2
def achaNega() -> None:
    for i in range (0,5,1):
        if v[i] < 0:
            print(v[i])

#EXERCÍCIO 3
def somaVet(vet: list) -> float:
    soma=0
    for i in range (0,5,1):
        soma = soma + vet[i]
    return soma

#EXERCÍCIO 4
def mediaVet(vet) -> float:
    # soma = 0
    # for i in range (0,5,1):
    #     soma = soma + v[i]
    # media = soma / 5 
    return somaVet(vet)/5

#EXERCÍCIO 5
def achaImpar(v) -> int:
    for i in range (0,5,1):
        if v[i]%2==1:
            print(v[i]) 

#EXERCÍCIO 6
def exiba_extremos(v):
    print(v[0],v[-1])

#EXERCÍCIO 7
def exibe_indice_par(v):
    for i in range(5):
        if i % 2 == 0:
            print(v[i])

#EXERCÍCIO 8
def existeOuNao(v: list, valor: int) -> bool:
    for i in range(5):
        if valor==v[i]:
            return True
    else:
        return False
        
#EXERCÍCIO 9
def ordenaVetor(v):
    for i in range(5):
        for j in range(5):
            if v[i]<v[j]:
               save = v[i]
               v[i] = v[j]
               v[j] = save
    for y in range(5):
        print(v[y])

#EXERCÍCIO 10
def copiaVet(v1: list, v2: list) -> list:
    for i in range(5):
        v2[i]=v1[i]
    for i in range(5):
        print(f"v2={v2[i]}\n")

#EXERCÍCIO 11
def inverte_vetor(v1: list, v2: list):
    for i in range(5):
        v2[i]=v1[4-i]
    for i in range(5):
       print(f"v1={v1[i]}   v2={v2[i]}\n")

#EXERCÍCIO 12
def ordena_vetor_crescente(vet: list) -> list:
    for i in range(5):
        for j in range(5):
            if vet[i]<vet[j]:
               save = vet[i]
               vet[i] = vet[j]
               vet[j] = save
    for y in range(5):
        print(vet[y])


#EXERCÍCIO 13
def ordena_vetor_decrescente(vet):
    for i in range(5):
        for j in range(5):
            if vet[i]>vet[j]:
               save = vet[i]
               vet[i] = vet[j]
               vet[j] = save
    for y in range(5):
        print(vet[y])

#EXERCÍCIO 14
def ordena_vetor_geral(vet: list, opcao: str):
    if opcao == 'c':
        for i in range(5):
            for j in range(5):
                if vet[i]<vet[j]:
                    save = vet[i]
                    vet[i] = vet[j]
                    vet[j] = save
        for y in range(5):
            print(vet[y])
    elif opcao == 'd':
        for i in range(5):
            for j in range(5):
                if vet[i]>vet[j]:
                    save = vet[i]
                    vet[i] = vet[j]
                    vet[j] = save
        for y in range(5):
            print(vet[y]) 

#EXERCÍCIO 15
def separaParesImpares(vet: list):
    for i in range(5):
        for j in range(5):
            if vet[i]%2==0:
                save=vet[i]
                vet[i]=vet[j]
                vet[j]=save
    for i in range(5):            
        print(vet[i])
        
#EXERCÍCIO 16
def acima_media(vet: list) -> int:
    x=0
    media=mediaVet(vet)
    for i in range(5):
        if vet[i]>media:
            x=x+1
    return x

#EXERCÍCIO 17
def maior_elemento(vet: list) -> int:
    x=0
    for i in range(5):
        if vet[i] > x:
            x=vet[i]
    return x