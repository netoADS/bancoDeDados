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

# solicitando a entrada do usuário
busca = input("Digite o nome que deseja buscar: ")

# executando a consulta com LIKE
sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%" + busca + "%",)
cursor.execute(sql, val)

# obtendo os resultados
results = cursor.fetchall()

# iterando sobre os resultados
for result in results:
  print(result)
# Fechar a conexão e o cursor
conn.close()
