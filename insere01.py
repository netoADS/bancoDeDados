from conexao import conectar

# chama a funçao conectar
conn = conectar()

# Estabelecer a conexão com o banco de dados
try:
    conn = conn
    print("Conexão executada com sucesso.")
except conn.connector.Error as err:
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