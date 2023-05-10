# Aula 23 - Filtros com Where
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

# sql = "SELECT * FROM custormes WHERE address = 'São Paulo, SP'"

sql = "SELECT * FROM custormes WHERE address LIKE '%a%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
