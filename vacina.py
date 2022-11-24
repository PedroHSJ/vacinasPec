import mariadb
import psycopg2
from insertVacina import insertVacina
from selectVacina import selectVacina
from enviarEmail import enviarEmail


def vacina2anos(codibge, dbname):
    try:
       
        print("Iniciando conexão com o banco de dados PEC...")
        connectionPEC = psycopg2.connect(
        dbname="esus",
        user="postgres",
        password="esus",
        host="177.200.36.111",
        port="5433",
        )
        cursorPEC = connectionPEC.cursor()
        cursorPEC.execute(selectVacina(codibge))
        print("Select Vacina realizado com sucesso")
    
        numero_linhas = 0

        array = []
        
        for data in cursorPEC:
            array.append(data)
            numero_linhas += 1
        print("Número de linhas: ", numero_linhas)
        connectionPEC.commit()
        cursorPEC.close()
        connectionPEC.close()
        print("Conexão com o banco de dados PEC encerrada")

        print("Numero de linhas: ", numero_linhas)
        print(f'''Iniciando conexão com o banco de dados ESUSATENDSAUDE: 
            user="pedro",
            password="1q2w3e4r",
            host ="dbhd.esusatendsaude.com.br",
            port=3306,
            database="{dbname}",
        ''')
        connectionATENDSAUDE = mariadb.connect(
            user="pedro",
            password="1q2w3e4r",
            host ="dbhd.esusatendsaude.com.br",
            port=3306,
            database=dbname,
        )
        cursorATENDSAUDE = connectionATENDSAUDE.cursor()

        cursorATENDSAUDE.execute("TRUNCATE TABLE vacinas_pec")
        print("Tabela vacinas_pec truncada.")
        print("Inserindo dados na tabela vacinas_pec...")
    
        cursorATENDSAUDE.executemany(insertVacina(), array)
        
        connectionATENDSAUDE.commit()
        print("Dados inseridos com sucesso.")
        cursorATENDSAUDE.close()
        connectionATENDSAUDE.close()
        print(f"Conexão com o banco de dados ESUSATENDSAUDE {dbname} encerrada.")

    except psycopg2.Error as e:
        print(f"Erro no banco do PEC: {e}")
        enviarEmail(e, 'PEC')
    except mariadb.Error as e:
        print(f"Erro no banco {dbname}: {e}")
        enviarEmail(e, dbname)
