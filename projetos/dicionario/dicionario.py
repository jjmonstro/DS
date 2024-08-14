import os 
os.system("cls")

crias = {
    'nome' : 'Correx',
    'crime' : 244,
    'estado civil' : 'Delas',
    'gay' : True
}

#Exibir de forma digna
print(f"Nomes: {crias['nome']}")
print(f"Crime: {crias['crime']}")
print(f"Estado Civil: {crias['estado civil']}")
print(f"Gay ?: {crias['gay']}")

crias['pente'] = 'Adaptado'
os.system("cls")
print(list(crias.items()))

for k, v in crias.items():
    print(f"{k} -> {v}")
