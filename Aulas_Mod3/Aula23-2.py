# Aula sem numero - Organização com Order By
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

# sql = "SELECT name FROM custormes ORDER BY name"
sql = "SELECT name FROM  custormes ORDER BY name DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
