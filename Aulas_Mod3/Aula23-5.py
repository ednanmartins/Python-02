# Aula sem numero - Exclusão de tabelas
import mysql.connector as MySQL

#   Configuração do Banco
mydb = MySQL.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase",
)

#   Teste de Conexão e criação do cursor
if mydb.is_connected:
    print("Pelo menos aqui foi, grazadeus")
    mycursor = mydb.cursor()

sql = "DROP TABLE custormes"

mycursor.execute(sql)
print("Tabela viajou!!!")
