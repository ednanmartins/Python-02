# Aula 22 - Consultas com Select
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

mycursor.execute("SELECT * FROM custormes")


myresult = mycursor.fetchall()
for x in myresult:
    print(x)

myresult = mycursor.fetchone()
print(myresult)
