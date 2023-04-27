import mysql.connector

# Conectando ao banco de dados
config = {
  'user': 'admin',
  'password': 'aulanoiteFaculdade',
  'host': 'dbaula.clstmfvvjfyt.us-east-1.rds.amazonaws.com',
  'database': 'aula'
}

#Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print(f"Conexão executada como sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
#criando um objeto cursor para executaar as consultas SQL
cursor = conn.cursor()

#pedindo ao usuário o nome e código do estado
nome_estado = input("Digite o nome do estado: ")
codigo_estado = int(input("Digite o código do estado: "))

# Inserindo o estado na tabela
sql = "INSERT INTO estado (codigo, nome) VALUES (%s, %s)"
val = (codigo_estado, nome_estado)
cursor.execute(sql, val)

# Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão e o cursor
conn.close()