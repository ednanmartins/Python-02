'''Crie uma base de dados MongoDB contendo as seguintes coleções e suas respectivas quantidades de documentos:
Coleções
Livros: 20 documentos.
Revistas: 15 documentos.
Jornais: 15 documentos.
Mangás: 10 documentos.

Todos os documentos devem ter pelo menos 4 campos.
Deverá haver documentos com mais e menos campos que os demais.
Deverá haver _id do tipo Object e declarados pelo usuário.
Devem haver campos dos tipos: Int, Double, String, ObjectId.'''


from pymongo import collection
from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = (
        "mongodb+srv://root:<WGRHIth3BzcSS4z1>@cluster0.tnzynwo.mongodb.net/"
    )

    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso!")
    return client["exPratico1"]


dbname = get_database()
collection_name = dbname["livros"]
