import os
os.system("cls")

stringList=["abc"]
lista=[2,4,5,7,9]

def transformaVogal(s:list):
    string=s.replace('a', 'A')
    string=string.replace('e', 'E')
    string=string.replace('i', 'I')
    string=string.replace('o', 'O')
    string=string.replace('u', 'U')
    print(string)

    
def inteiroOUnao(l:list) -> bool:
    for i in l:
        if type(i) == str and i.isdigit:
            a=False
            break
        else:
            a=True
        if i < 0:
            a=False
            break
    return a

    
def true_true(l) -> bool:
    
    # for i in range(len(l)):
    #     if l[0] == "-" or l=="+" or numeros:
    #         a = True
    #     elif l[i + 1] == letras:
    #         a = False
    letras="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a=True
    for i in range(len(l)):
        if l[i] in letras:
            a = False
            break
    return a


# print(true_true(stringList))
# transformaVogal(string)
print(inteiroOUnao(lista))