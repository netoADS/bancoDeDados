import mysql.connector

# Conectando ao banco de dados
config = {
  'user': 'admin',
  'password': 'aulanoiteFaculdade',
  'host': 'dbaula.clstmfvvjfyt.us-east-1.rds.amazonaws.com',
  'database': 'aula'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

#inserindo o estado na tabela
sql = "SELECT * FROM estado"
cursor.execute(sql)

#obter o resultado da consulta
result = cursor.fetchall()
print(result)

for l in result:
    print(l)

conn.close()