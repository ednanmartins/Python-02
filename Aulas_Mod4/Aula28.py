#   Aula 28 - Atualização de dados

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

#atualiza desconto_maximo de 10% para 35%.
collection_name.update_many({"disconto_maximo":"10%"}, {"$set":{"disconto_maximo": "35%"}})

#atualiza desconto para 100% onde nome_item tenha a palavra 'Aula'
collection_name.update_one({"nome_item": {"$regex": "Aula"}}, {"$set":{"disconto_maximo": "100%"}})


detalhes_itens = collection_name.find()
for item in detalhes_itens:
    print(item)