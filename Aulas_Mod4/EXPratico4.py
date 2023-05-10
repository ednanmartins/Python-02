'''EXERCÍCIO PRÁTICO
1- Crie um script contendo cinco funções:
    a.Criar itens, onde o usuário pode selecionar a quantidade de campos;
    b.Mostrar todos os documentos;
    c.Deletar documentos pelo ID;
    d.Deletar toda a coleção do banco de dados;
    e.Atualizar documentos por ID ou por campos.
OBS: Não precisa criar menu para escolha das funções, elas podem ser chamadas separadamente.'''

from pymongo import collection
from pymongo import MongoClient


def criar_db():
    CONNECTION_STRING = (
        "mongodb+srv://root:<WGRHIth3BzcSS4z1>@cluster0.tnzynwo.mongodb.net/"
    )

    client = MongoClient(CONNECTION_STRING)
    print("Criado/Conectado com sucesso!")
    return client["exPratico"]


def cadastrar_itens():
    dbname = criar_db()
    collection = dbname["exercicios"]

    n = int(input('Quantos campos terá seu doc? '))
    d = dict(input('Digite a chave e o valor separafo poe espeços: ').split() for _ in range(n))
    print(d)
    collection.insert_one(d)
    print('Docs inseridos com sucesso!')

def mostrar_tudo():
    dbname = criar_db()
    collection = dbname["exercicios"]

    detalhes_itens = collection.find()
    for item in detalhes_itens:
        print(item)

def deletar_por_id():
    dbname = criar_db()
    collection = dbname["exercicios"]

    id = str(input('Digite o id de quem deseja deletar: '))
    collection.delete_one({"_id" : id})
    print('Dados deletados!')
    
def deletar_colletion():
    dbname = criar_db()
    collection = dbname["exercicios"]

    perg = str(input("Certesa que quer deletar Colletion? S/N: "))

    if (perg == 'S' or 'Sim'):
        collection.drop()
        print('Colação deletada!')
    elif (perg =='N' or 'Nao' or "Não"):
        print('Blz, então deixa pra lá!!!')
    else:
        print('Naam, opção invalida!!')

def atualizar_dados():
    dbname = criar_db()
    collection = dbname["exercicios"]

    perg = str(input('Como deseja alterar?'
                     '\n1-Atualizar por ID: '
                     '\n2-Atualizar por Campo: '))
    if (perg=="1"):
        id = str(input("Digite o ID as ser alterado: "))
        chave = str(input("Digite o campo a ser aletrado: "))
        valor = str(input("Digite o novo valor do campo digitado: "))

        collection.update_one({"_id":id}, {"$set":{chave:valor}})
        print("Modificação realizada!")

    elif (perg=="2"):
        chave = str(input("Digite a chave a ser buscada: "))
        valor = str(input("Digite o valor a ser buscado: "))
        chave2 = str(input("Digite a chave a ser alterada: "))
        valor2 = str(input("Digite o novo valor: "))

        collection.update_many({chave:valor}, {"$set":{chave2:valor2}})
        print("Modificação realizada!")


#cadastrar_itens()
#mostrar_tudo()
#deletar_por_id()
#deletar_colletion()
atualizar_dados()
