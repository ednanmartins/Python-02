#   Aula 29 - Exclusão  de Dados

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

#Exclui documento cujo ID é SC004
collection_name.delete_one({"_id" : "SC001"})
print('Dados deletados!')

#Deleta todos os documentos
collection_name.drop()
dbname.drop_collection()


detalhes_itens = collection_name.find()
for item in detalhes_itens:
    print(item)