import os
import json
os.system("cls")

pessoas = {
    'pessoa1':{
        'nome': 'Correx',
        'idade': 99,
        'email': 'jpcorreia1211@gmail.com'
    },
    'pessoa2':{
            'nome': 'Tenorio Tesoura',
            'idade': 19,
            'email': 'TenasPenas@gmail.com'
        },
}

file_path="D:\JoaoMatheus2AI\DS\explicacoes\\arq_json\\arquivo.json"

print(pessoas)
pessoas_json = json.dumps(pessoas, indent=4)
print("Exibindo o dicionário...\n")
print(pessoas)
print("Exibindo o objeto json...\n")
print(pessoas_json)

# Gravando no arquivo json
with open(file_path, "w", encoding="utf-8") as file:
    # Gravando o objeto json on arquivo
    file.write(pessoas_json)

# Lendo um arq json
with open(file_path, "r", encoding="utf-8") as file:
    print("\nexibindo o arq json...")
    pessoas_json = file.read()
    pessoas = json.loads(pessoas_json)

for k, v in pessoas.items():
    print(f"Registro....: {k}")
    for k1, v1 in v.items():
        print("\t" + k1 + ":" + str(v1))

