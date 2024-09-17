import os 
os.system("cls")

notas = {'Joao': 9.5,
         'jj': 10.5,
         'pp': 11.5}

print(notas["Joao"])
notas.update([('pp',10.5)])
print(notas)
notas.clear() 
print(notas)
