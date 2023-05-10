# Aula sem numero - Atualização de dados
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

sql = "UPDATE custormes SET address='Manaus, AM' WHERE address='Palmas, TO'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "linha(s) afetada(s)!")
