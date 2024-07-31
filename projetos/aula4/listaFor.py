import os 
os.system("cls")

a=0
mediaS = 0
aoMenos9 = 0
for i in range(1,11,1):
    a=a+1
    nota1 = float(input(f"Digite a primeira nota do aluno {a}: "))
    while nota1 > 10 or nota1 < 0:
        print("Nota INVALIDA")
        nota1 = float(input("Por favor digite novamente: "))

    nota2 = float(input(f"Digite a segunda nota do aluno {a}: "))
    while nota2 > 10 or nota2 < 0:
        print("Nota INVALIDA")
        nota2 = float(input("Por favor digite novamente: "))

    nota3 = float(input(f"Digite a terceira nota do aluno {a}: "))
    while nota3 > 10 or nota3 < 0:
        print("Nota INVALIDA")
        nota3 = float(input("Por favor digite novamente: "))
    
    if nota1 < nota2  and nota1 < nota3:
        media = (nota2 + nota3) / 2
        if media >= 9:
            aoMenos9 = aoMenos9 + 1

        mediaS = media + mediaS

    elif nota2 < nota3:
        media = (nota3 + nota1) / 2
        if media >= 9:
            aoMenos9 = aoMenos9 + 1

        mediaS = media + mediaS

    else:
        media = (nota1 + nota2) / 2
        if media >= 9:
            aoMenos9 = aoMenos9 + 1

        mediaS = media + mediaS
        
mediaS = mediaS/10    
print(f"A média da sala é {mediaS} e {aoMenos9} alunos tiraram ao menos 9 de média")



    

    