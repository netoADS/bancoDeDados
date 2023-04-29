from conexao import conectar

def listar(conn, cursor):
    #abrir uma conecao com o banco de dados
    conn = conectar()
    #criando um objeto cursor para executar as consultas sql
    cursor = conn.cursor()
    #executar a consulta sql para listar os registros
    cursor.execute("SELECT * FROM estado")
    #obter os resultados
    resultados = cursor.fetchall()
    #imprimir os resultados
    for r in resultados:
        print(r)
    
     # Fechar a conezao e o cursor    
    cursor.close()
    conn.close()
    
def inserir(codigo, nome):
    #abrir uma conecao com o banco de dados
    conn = conectar()
    
    #criando um objeto cursor para executar as consultas sql
    cursor = conn.cursor()
    
    #executar a consulta sql para inserir um novo registro
    sql = "INSERT INTO estado (codigo, nome) VALUES (%s, %s)"
    val = (codigo, nome)
    
    #commit da transação
    conn.commit()
    
    #imprimir mensagem de sucesso
    print("Registro inserido com sucesso")
    
    # Fechar a conezao e o cursor
    cursor.close()
    conn.close()
    
def atualizar(codigo, novo_nome):
    #abrir uma conecao com o banco de dados
    conn = conectar()
    
    #criando um objeto cursor para executar as consultas sql
    cursor = conn.cursor()
        
    #executar a consulta sql para atualizar o registro
    sql = "UPDATE estado SET nome = %s WHERE codigo = %s"
    val = (novo_nome, codigo)
    cursor.execute(sql,val)
        
    #commit da transação
    conn.commit()
        
    #verifica se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")
        
    # Fechar a conezao e o cursor
    cursor.close()
    conn.close()
    
def apagar(codigo):
    #abrir uma conecao com o banco de dados
    conn = conectar()
    
    #criando um objeto cursor para executar as consultas sql
    cursor = conn.cursor()
        
    #executar a consulta sql para deletar o registro
    sql = "DELETE FROM estado WHERE codigo = %s"
    val = (codigo,)
    cursor.execute(sql,val)
    
    #commit da transação
    conn.commit()
    
    #verifica se algum registro foi deletado
    if cursor.rowcount == 0:
        print("Nenhum registro deletado.")
    else:
        print("Registro deletado com sucesso.")
       
    # Fechar a conezao e o cursor
    cursor.close()
    conn.close()
    
conn = conectar()
#criando um objeto cursor para executar as consultas sql
cursor = conn.cursor()
while True:
    print("O que voce deseja fazer?")
    print("1 - Listar estados")
    print("2 - Inserir novo estado")
    print("3 - Atualizar um estado")
    print("4 - Deletar um estado")
    print("0 - Sair")
    
    opcao = int(input("Digite o numero de opção desejada: "))
    
    if opcao == 1:
        listar(conn, cursor)
    elif opcao == 2:
        codigo = int(input("Digite o codigo do novo estado: "))
        nome = input("Digite o nome do novo estado: ")
        inserir(codigo, nome)
    elif opcao == 3:
        codigo = int(input("Digite o codigo do estado que deseja atualizar: "))
        nome = input("Digite o nome do estado: ")
        atualizar(codigo, nome)
    elif opcao == 4:
        codigo = int(input("Digite o codigo do estado que deseja deletar: "))
        apagar(codigo)
    elif opcao == 0:
        break
    else:
        print("Opçao invalida. Digite novamente.")