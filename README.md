# Projeto: Consultas Médicas Especializadas de Porto Alegre - RS

Este projeto tem como objetivo realizar operações de ETL (Extract, Transform, Load) e CRUD (Create, Read, Update, Delete) em um banco de dados MySQL utilizando Python. O conjunto de dados utilizado refere-se às solicitações de consultas médicas especializadas na cidade de Porto Alegre, RS.

## Estrutura do Projeto

O projeto está dividido em duas partes principais:

1. **P1: ETL (Extract, Transform, Load)**
   - **Objetivo:** Carregar, tratar e inserir os dados em um banco de dados MySQL.
   - **Documento:** [P1_SaudePOA_ETL.ipynb](P1_SaudePOA_ETL.ipynb)
   - **Descrição:** Nesta etapa, os dados são extraídos de um arquivo CSV, transformados (limpeza, tipagem, tratamento de caracteres especiais, etc.) e carregados em um banco de dados MySQL.

2. **P2: CRUD (Create, Read, Update, Delete)**
   - **Objetivo:** Realizar operações de CRUD no banco de dados MySQL.
   - **Documento:** [P2_SaudePOA_CRUD.ipynb](P2_SaudePOA_CRUD.ipynb)
   - **Descrição:** Esta etapa permite a inserção, leitura, atualização e exclusão de registros no banco de dados. As operações são realizadas por meio de funções definidas no script [P2_funcoes_database.py](P2_funcoes_database.py).

## Como Utilizar

### P1: ETL
1. Execute o notebook [P1_SaudePOA_ETL.ipynb](P1_SaudePOA_ETL.ipynb).
2. O notebook realizará a extração, transformação e carga dos dados no banco de dados MySQL.

### P2: CRUD
1. Execute o notebook [P2_SaudePOA_CRUD.ipynb](P2_SaudePOA_CRUD.ipynb).
2. Escolha a operação desejada:
   - **1 - Inserir um registro**
   - **2 - Ler os registros**
   - **3 - Atualizar um registro**
   - **4 - Deletar um registro**
   - **5 - Encerrar operações**
3. Siga as instruções apresentadas para realizar a operação escolhida.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pandas`
  - `numpy`
  - `sqlalchemy`
  - `mysql-connector-python`
- Banco de dados MySQL

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/JHOliveira94/SaudePOA_ETL_CRUD.git
2. Instle as dependências
   ```bash
   pip install pandas numpy sqlalchemy mysql-connector-python
3. Configure o banco de dados MySQL com as credenciais fornecidas no script P2_funcoes_database.py.

**Melhorias Futuras**
- **Automação de ETL:** Implementar Web Scraping para buscar automaticamente os arquivos de dados no site.
- **Refatoração do Código:** Melhorar o desempenho do código, especialmente na leitura inicial e na carga dos dados no MySQL.
- **Segurança:** Utilizar variáveis de ambiente para armazenar credenciais do banco de dados.
- **Personalização de Queries:** Permitir a inserção de queries específicas nas operações CRUD.
- **CLI (Command Line Interface):** Construir uma interface de linha de comando para uma experiência mais padronizada.

## Conclusão
Este projeto demonstra a capacidade de realizar operações de ETL e CRUD em um banco de dados MySQL utilizando Python.<br>
As etapas de extração, transformação e carga foram realizadas com sucesso, e as operações de CRUD estão funcionais, permitindo a manipulação dos dados de forma eficiente.

Para mais informações, entre em contato com o autor:<br>
**AUTOR:** José Henrique de Oliveira<br>
**LINKEDIN:** [jholiveira94](https://www.linkedin.com/in/jholiveira94/)<br>
**GITHUB:** [JHOliveira94](https://github.com/JHOliveira94)
