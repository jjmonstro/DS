import os
#joao pedro correia
registro = [
    {
        'CPF' : 54304508806,
        'Nome' : 'Joao',
        'Idade' : 22
    }
]

#sub
def verificaCPF(CPF: str) -> bool:
    for linha in registro:
        if linha["CPF"] == CPF:
            input("CPF já existente!!\n")  
            return False
        else:
            return True
    
def cpf_existe(CPF: int):
    for linha in registro:
            if linha['CPF'] == CPF:
                return True

            else:
                continue
    return False
        
def verificaNome(n: str) -> bool:
     if n == '':
          print("Nome inválido!!\n")
          return False
     n=n.capitalize()
     schar='!@#$%¨&*()_+=-/¬¢£.,><;:][}{?\|\'\"][ªº°'
     for i in n:
        if i.isnumeric() or i in schar:
            print("Nome inválido!!\n")
            return False
        else:
            return True


while True:
    CPF = input("CPF: ")
    if CPF=="":
        break
    try:
        CPFI=int(CPF)
    except:
        print("CPF inválido")
        continue

    if cpf_existe(CPFI):
        for linha in registro:
            print(f"Nome: {linha['Nome']}")
            print(f"Idade: {linha['Idade']}")
            while True:
                nome=input("Nome: ")
                if not verificaNome(nome):
                    continue
                else:
                    break
            
            while True:
                idade=input("Idade: ")
                try:
                    idade=int(idade)
                    break
                except:
                    print("Idade inválida!!\n")  
                    continue
            #esse update não esta funcionando
            registro[linha.update(CPF,nome,idade)]
            print(registro)
            print("Cadastrado com sucesso!!")
            continue

    else:
        while True:
            nome=input("Nome: ")
            if not verificaNome(nome):
                continue
            else:
                break

        while True:
            idade=input("Idade: ")
            try:
                idade=int(idade)
                break
            except:
                print("Idade inválida!!\n")  
                continue
        novo_registro = {
            'CPF' : CPF,
            'Nome' : nome,
            'Idade' : idade
        }
      
        registro.append(novo_registro)
        print("Cadastrado com sucesso!!")
        continue
            

