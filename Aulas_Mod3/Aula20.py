# Aula 20 - Criando database e table
import mysql.connector as MySQL

mydb = MySQL.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase",
)

if mydb.is_connected:
    print("Pelo menos aqui foi, grazadeus")
    mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# print("Foi criada!")

"""mycursor.execute(
    "CREATE TABLE custormes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255))"
)"""
print("Tabela criada")
