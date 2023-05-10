#   Exercicio Pratico
"""1-Crie uma base de dados chamada sistema_escolar_soul_on
2-Crie uma tabela alunos com os campos id, nome, matricula, turma.
3-Alimente a tabela com os seguintes dados:
4-Faça as seguintes consultas:
    a·Liste todos os registros de sua tabela.
    b·Liste apenas nome e matrícula dos alunos do BCW23.
    c·Liste apenas o nome dos alunos que tiverem o sobrenome Lima.
5-O aluno Carlos Augusto está na turma errada. Matricule o mesmo no BCW25.
6-O aluno José Vinicius desistiu do curso, ele deve ser excluído do sistema.

*Se preferir, pode usar funções para evitar exclusões."""

import mysql.connector as MySQL


def criar_database():
    mydb = MySQL.connect(
        host="localhost",
        user="root",
        password="",
    )
    mycursor = mydb.cursor()
    mycursor.execute(criar_db)
    print("Database criada com sucesso!")


#   Configuração do Banco
mydb = MySQL.connect(
    host="localhost",
    user="root",
    password="",
    database="sistema_escolar_soul_on",
)

#   Teste de Conexão e criação do cursor
if mydb.is_connected:
    print("Pelo menos aqui foi, grazadeus")
    mycursor = mydb.cursor()

# criar_database()

criar_db = "CREATE DATABASE sistema_escolar_soul_on"
criar_tabela = "CREATE TABLE alunos(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), matricula VARCHAR(255), turma VARCHAR(255))"
alimenta_tabela = "INSERT INTO alunos (nome, matricula, turma) VALUES (%s, %s, %s)"
dados_tabela = [
    ("José Lima", "MAT90551", "BCW22"),
    ("Carlos Augusto", "MAR90552", "BCW22"),
    ("Livia Lima", "MAT90553", "BCW22"),
    ("Sandra Gomes", "MAT90554", "BCW23"),
    ("João Augusto", "MAT90555", "BCW23"),
    ("Breno Lima", "MAT90556", "BCW24"),
    ("José Vinicius", "MAT90557", "BCW25"),
]
mostrar_tudo = "SELECT * FROM alunos"
mostrar_bcw23 = "SELECT nome, matricula FROM alunos WHERE turma = 'BCW23'"
mostrar_lima = "SELECT nome FROM alunos WHERE nome LIKE '%Lima'"
atualiza_turma = "UPDATE alunos SET turma='BCW25' WHERE nome='Carlos Augusto'"
desistente = "DELETE FROM alunos WHERE nome='José Vinicius'"

mycursor.execute(desistente)
# mycursor.executemany(alimenta_tabela, dados_tabela)    #executar mais de 1 argumento
print(mycursor.rowcount, "linha(s) alterada(s) com sucesso!\n\n")
mydb.commit()  # so precisa quando tem alguma alteração na tabela

mycursor.execute(mostrar_tudo)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
