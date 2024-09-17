registro = [
    {
        'CPF' : 54304508806,
        'Nome' : 'Joao',
        'Idade' : 22
    }
]

def cpf_existe(CPF: str):
    for linha in registro:
            if linha['CPF'] == CPF:
                print(linha['Nome'])
                print(linha['Idade'])
            else:
                continue
    return False
cpf_existe(54304508806)

            