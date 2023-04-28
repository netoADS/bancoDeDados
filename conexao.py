import mysql.connector

def conectar():
    # Conectando ao banco de dados
    mydb = mysql.connector.connect(
        host="dbaula.clstmfvvjfyt.us-east-1.rds.amazonaws.com",
        user="admin",
        password="aulanoiteFaculdade",
        database="aula"
    )
    
    return mydb
