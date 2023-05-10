#   Aula 27 - Listagem de dados - parte 2

from pymongo import collection
from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = (
        "mongodb+srv://root:<WGRHIth3BzcSS4z1>@cluster0.tnzynwo.mongodb.net/"
    )

    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso!")
    return client["soul_code_db"]

dbname = get_database()
collection_name = dbname["itens_soulcode"]

#detalhes_itens = collection_name.distinct("nome_item")
# #detalhes_itens = collection_name.find({"categoria":"Físico"}).limit(1)
detalhes_itens = collection_name.find({}, {"nome_item", "desconto_maximo"}).skip(2)

for item in detalhes_itens:
    print(item)