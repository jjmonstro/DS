'''Joao Pedro Correia'''
def conta_acima_media(vet: list) -> int:
    soma=0
    a=0
    for i in range(5):
        soma=soma+vet[i]
    media=soma/5
    for i in range(5):
        if vet[i] > media:
            a=a+1 
    return a

def inverte_vetor(vet1: list, vet2: list):
    for i in range(5):
        vet2[i]=vet1[4-i]
    for i in range(5):
        print(f"vetor1- {vet1[i]}  vetor2- {vet2[i]}\n") 
