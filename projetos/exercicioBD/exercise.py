import os
import pyodbc
import pandas as pd
os.system("cls")

try:
    #config da conexão
    server = 'localhost'
    database = 'petshop'
    username = 'sa'
    password = '12112007'

    #estabelecer conexão
    conn = pyodbc.connect('DRIVER={SQL server}; SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_exclusao = conn.cursor()
    inst_exclusao_porId = conn.cursor()
    inst_alteracao = conn.cursor()
except Exception as e:
    print("Erro: ", e)
    conexao = False
else:
    conexao = True
    print("conexão efetuada com sucesso!!❤(☞ﾟヮﾟ)☞  ☜(ﾟヮﾟ☜)\n︻╦̵̵̿╤─ ҉ - - - - - - -")

while conexao:
    os.system("cls")
    print("""
    MENU
    0 - Sair
    1 - Cadastrar pets
    2 - Show pets
    3 - editar
    4 - Excluir um
    5 - Excluir todos
""")
    escolha = int(input("Escolha: "))
    os.system("cls")
    match escolha:
        case 0:
            break
        case 1:
            try:
                tipo=input('Tipo do pet.....:')
                nome=input('Nome do pet.....:')
                idade=int(input('Idade do pet..:'))

                cadastro=f"""
                INSERT INTO petshop (tipo_pet,nome_pet,idade)
                VALUES ('{tipo}','{nome}', {idade})
                """
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                print('Digite uma idae numerica')
            except Exception as e:
                print('Erro bb'+e)
            else:
                input("gravação efetuada com sucesso!!❤(☞ﾟヮﾟ)☞  ☜(ﾟヮﾟ☜)\n︻╦̵̵̿╤─ ҉ - - - - - - -")
        case 2:
            lista_dados = []
            inst_consulta.execute("SELECT * FROM petshop")
            data = inst_consulta.fetchall()
            print(data)
            for dt in data:
                lista_dados.append(dt)

            lista_dados = sorted(lista_dados)

            print(lista_dados)
            dados_df = pd.DataFrame.from_records(lista_dados, columns={'Id', 'Tipo', 'Nome', 'Idade'}, index='Id')

            if dados_df.empty:
                print("Não há pets cadastrados")
            else:
                print(dados_df)
            input("pressione enter...")
        case 3:
            #só exibindo deveria ser uma função mas estou com preguiça
            lista_dados = []
            inst_consulta.execute("SELECT * FROM petshop")
            data = inst_consulta.fetchall()
            print(data)
            for dt in data:
                lista_dados.append(dt)

            lista_dados = sorted(lista_dados)

            print(lista_dados)
            dados_df = pd.DataFrame.from_records(lista_dados, columns={'Id', 'Tipo', 'Nome', 'Idade'}, index='Id')

            if dados_df.empty:
                print("Não há pets cadastrados")
            else:
                print(dados_df)

            #de fato alterando
            try:
                id_pet = int(input('Digite o id do pet a ser alterado: '))
                tipo=input('Tipo do pet.....:')
                nome=input('Nome do pet.....:')
                idade=int(input('Idade do pet..:'))

                inst_alteracao.execute(f"UPDATE petshop SET tipo_pet='{tipo}', nome_pet='{nome}', idade={idade} WHERE id={id_pet}")
                conn.commit()
            except ValueError:
                print('Digite uma idae numerica')
            except Exception as e:
                print('Erro bb'+e)
            else:
                input("alteração efetuada com sucesso!!❤(☞ﾟヮﾟ)☞  ☜(ﾟヮﾟ☜)\n︻╦̵̵̿╤─ ҉ - - - - - - -")
        case 4:
            #só exibindo
            lista_dados = []
            inst_consulta.execute("SELECT * FROM petshop")
            data = inst_consulta.fetchall()
            print(data)
            for dt in data:
                lista_dados.append(dt)

            lista_dados = sorted(lista_dados)

            print(lista_dados)
            dados_df = pd.DataFrame.from_records(lista_dados, columns={'Id', 'Tipo', 'Nome', 'Idade'}, index='Id')

            if dados_df.empty:
                print("Não há pets cadastrados")
            else:
                print(dados_df)
            

            #de fato excluindo (ele exclui aqui no python mas lá no banco não exclui de fato＼（〇_ｏ）／)
            inst_exclusao_porId.execute(f"DELETE FROM petshop WHERE id={int(input('Digite o id do pet a ser excluido: '))}")
            conn.commit()
        case 5:
            inst_exclusao.execute("DELETE FROM petshop")
        case _:
            input('opçao invalida')