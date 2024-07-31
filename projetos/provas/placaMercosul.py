import os
os.system ("cls")

#---------------------fucktions
def placa(s: str) -> bool:
    numeros="0123456789"
    letras="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valido = True
    if len(s) != 7:
        valido = False
        return valido
    else:
        slista=list(s)
        slista[3], slista[4] = slista[4], slista[3]  
        for i in range(3):
            if slista[i] not in letras:
                valido = False
                break
        for i in range(4,6):
            if slista[i] not in numeros:
                valido = False
                break
    return valido

            
       
#---------------------Main Program
print(placa("ABC5D67")) #true
print(placa("ABC5D6")) #false
print(placa("1234567")) #false
print(placa("ABC5D678")) #false
print(placa("AB@5D67")) #false
print(placa("ABC@D67")) #false
print(placa("aBC5d71")) #true

