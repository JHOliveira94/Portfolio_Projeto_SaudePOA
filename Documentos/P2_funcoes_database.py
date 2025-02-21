# Sobre este script
# Nesse documento, estão definidas as funções  necessárias para operações CRUD em banco MySQL usando python
# Para realização das operações, use o documento P2_SaudePOA_CRUD.ipynb

import pandas as pd
import mysql.connector
from mysql.connector import Error

# Configurações de acesso ao banco de dados
config = {
    'user': 'root',
    'password': '332654',
    'host': 'localhost',
    'database': 'projeto_saudepoa',
    'raise_on_warnings': True
}

# Tabela que sofrerá operações CRUD 
nome_tabela = 'tbl_solicitacoes_2024_tratada'

def conectar():
    """Conecta ao banco de dados MySQL.
    Usa as credenciais da variável confg.
    Função de apoio para execução das funções de operação."""

    try:
        conexao = mysql.connector.connect(**config)
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def obter_colunas_tabela(nome_tabela):
    """Obtém os nomes das colunas da tabela na variável nome_tabela.
    Permite versatilidade e garante funcionamento do código, visto que os nomes podem ser alterados."""

    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(f"DESCRIBE {nome_tabela}")
            colunas = [coluna[0] for coluna in cursor.fetchall()]
            return colunas
        except Error as e:
            print(f"Erro ao obter colunas da tabela: {e}")
            return []
        finally:
            cursor.close()
            conexao.close()
    return []


def inserir_registro():
    """Insere um novo registro na tabela.
    Permite ao usuário escolher as colunas que serão preenchidas.
    As colunas não preenchidas serão automaticamente None"""
    
    print('\nOperação escolhida: 1 - Inserir um registro\n')

    colunas = obter_colunas_tabela(nome_tabela)
    if not colunas:
        print("Não foi possível obter as colunas da tabela.")
        return

    # Exibir a lista de colunas com índices para escolha do usuário
    print("Escolha as colunas para preencher:")
    for i, coluna in enumerate(colunas[1::]): #Retira coluna de id_registro que é autopreenchida
        print(f"{i} - {coluna}")
    print("x - Preencher todas as colunas")

    # Coletar as escolhas do usuário
    escolhas = input("Digite os números das colunas separados por vírgula (ex: 1,2,3): ").strip().split(',')

    valores = {}

    if 'x' in escolhas: # Caso usuário queira preencher todas as colunas
        for coluna in colunas:
            valor = input(f"Digite o valor para {coluna}: ").strip()
            valores[coluna] = valor if valor else None  # Deixa como None se o valor for vazio
    else: # Preencher apenas as colunas selecionadas
        for escolha in escolhas:
            escolha = int(escolha.strip())
            if 1 <= escolha < len(colunas):
                coluna = colunas[escolha]
                valor = input(f"Digite o valor para {coluna}: ").strip()
                valores[coluna] = valor if valor else None  # Deixa como None se o valor for vazio

    # Query SQL
    colunas_selecionadas = [coluna for coluna in valores.keys()]
    placeholders = ['%s'] * len(colunas_selecionadas)
    query = f"INSERT INTO {nome_tabela} ({', '.join(colunas_selecionadas)}) VALUES ({', '.join(placeholders)})"

    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(query, tuple(valores.values()))
            conexao.commit()
            print("\n-> Registro inserido com sucesso!")
        except Error as e:
            print(f"Erro ao inserir registro: {e}")
        finally:
            cursor.close()
            conexao.close()


def ler_registros():
    """Lê registros da tabela e retorna um DataFrame Pandas."""

    print('\nOperação escolhida: 2 - Ler um registro\n')

    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = f"SELECT * FROM {nome_tabela}"
            cursor.execute(query)
            
            # Obtém os registros e os nomes das colunas
            registros = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
            
            # Cria um DataFrame do Pandas
            df = pd.DataFrame(registros, columns=colunas)
            
            print("\nRegistros encontrados:\n")
            display(df)
            return df  # Também retorna o DataFrame para uso posterior
        except Error as e:
            print(f"Erro ao ler registros: {e}")
            return None
        finally:
            cursor.close()
            conexao.close()
    return None

def atualizar_registro():
    """Atualiza um registro específico.
    Deve-se apresentar o id_registro para selecionar a linha.
    Após, indicar a coluna que receberá novo valor."""

    print('\nOperação escolhida: 3 - Atualizar um registro\n')

    id_valor = input(f"Digite o id_registro da linha que será deletada: ")
    print(f"Escolhido id_registro: {id_valor}")
    
    colunas = obter_colunas_tabela(nome_tabela)
    print("\nEscolha a coluna a ser atualizada:")
    for i, coluna in enumerate(colunas):
        print(f"{i} - {coluna}")
    escolha = int(input("Digite o número da coluna: "))
    coluna_alterar = colunas[escolha]
    novo_valor = input(f"Digite o novo valor para {coluna_alterar}: ")
    
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = f"""UPDATE {nome_tabela} SET {coluna_alterar} = %s WHERE id_registro = %s"""
            cursor.execute(query, (novo_valor, id_valor))
            conexao.commit()
            print("\n-> Registro atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar registro: {e}")
        finally:
            cursor.close()
            conexao.close()


def deletar_registro():
    """Deleta um registro pelo identificador único id_registro."""

    print('\nOperação escolhida: 4 - Deletar um registro\n')

    id_valor = input(f"Digite o id_registro da linha que será deletada: ")
    print(f"Escolhido id_registro: {id_valor}")
    
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = f"DELETE FROM {nome_tabela} WHERE id_registro = %s"
            cursor.execute(query, (id_valor,))
            conexao.commit()
            print("\n-> Registro deletado com sucesso!")
        except Error as e:
            print(f"Erro ao deletar registro: {e}")
        finally:
            cursor.close()
            conexao.close()


def operacoes_crud():
    '''Orquestra as operações de CRUD'''

    while True:
        print(f'''\nOperações CRUD na tabela {nome_tabela}:
            1 - Inserir um registro
            2 - Ler os registros
            3 - Atualizar um registro
            4 - Deletar um registro
            5 - Encerrar operações''')

        operacao_crud = int(input('Digite o número correspondente à operação desejada: '))

        if operacao_crud == 1:
            inserir_registro()
            print("\nEncerrando operações CRUD.")
            break
        elif operacao_crud == 2:
            ler_registros()
            print("\nEncerrando operações CRUD.")
            break
        elif operacao_crud == 3:
            atualizar_registro()
            print("\nEncerrando operações CRUD.")
            break
        elif operacao_crud == 4:
            deletar_registro()
            print("\nEncerrando operações CRUD.")
            break
        elif operacao_crud == 5:
            print("Encerrando operações CRUD.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            operacao_crud = int(input('Digite o número correspondente à operação desejada: '))