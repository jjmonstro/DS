def true_true(l) -> bool:
    
    # for i in range(len(l)):
    #     if l[0] == "-" or l=="+" or numeros:
    #         a = True
    #     elif l[i + 1] == letras:
    #         a = False
    letras=["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    a=True
    for i in range(len(l)):
        if l[i] in letras:
            a = False
            break
    return a


print(true_true("dd"))