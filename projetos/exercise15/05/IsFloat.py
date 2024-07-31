import os
os.system ("cls")

# --------- Funções
def eh_float(s: str) -> bool:
    slist=list(s)
    valido=True
    for i in range(len(slist)):
        if slist[i] == '.':
            valido=False
    return valido


# -------- Main
print(eh_float("345")) #True
print(eh_float("34.5")) #True
print(eh_float("34,5")) #False
print(eh_float("34.")) #True
print(eh_float("-345")) #True
print(eh_float("A34.5")) #False