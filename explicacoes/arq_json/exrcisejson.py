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

file_path="D:\JoaoMatheus2AI\DS\explicacoes\\arq_json\\arquivo2.json"

nome=str(input("Nome: joao joaquim"))
idade=str(input("Idade: "))
email=str(input("Email: "))


pessoas.update({'pessoa3':{
    'nome': 'dd',
    'idade': 99,
    'email': 'dd@gmail.com'
}})

print(pessoas)
pessoas_json = json.dumps(pessoas, indent=4)
with open(file_path, "w+", encoding="utf=8") as file:
    file.write(pessoas_json)



