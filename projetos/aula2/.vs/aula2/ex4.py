import os
os.system("cls")

quantmaca = int(input("Quantas maças você comprou?"))

if quantmaca < 12:
    valormaca = 0.30 
    valortotal = valormaca * quantmaca
    print(f"O valor total é isso {valortotal}")
else:
    valormaca = 0.25
    valortotal = valormaca * quantmaca
    print(f"O valor total é isso {valortotal}")



