# Aula 21 - Inserindo dados
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

sql = "INSERT INTO custormes (name, address) VALUES (%s, %s)"

"""val = ("José", "Piracuruca, PI")
mycursor.execute(sql, val)"""


val = [
    ("Pedro", "São Paulo, SP"),
    ("Ana", "Vitória, ES"),
    ("Débora", "Palmas, TO"),
    ("Clara", "São Bernardo, SP"),
    ("Sandy", "Ubajara, CE"),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "linha(s) alterada(s)")
