from conexao import conectar

# chama a funçao conectar
conn = conectar()

# Estabelecer a conexão com o banco de dados
try:
    conn = conn
    print("Conexão executada com sucesso.")
except conn.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

#inserindo o estado na tabela
sql = "SELECT * FROM estado"
cursor.execute(sql)

#obter o resultado da consulta
result = cursor.fetchall()
print(result)

# iterando sobre os resultados
for l in result:
    print(l)
    
# Fechar a conexão e o cursor
conn.close()