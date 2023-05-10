# Aula sem numero - Exclusão de dados
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Ubajara, CE'"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "linha(s) deletada(s).")