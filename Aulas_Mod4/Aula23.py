#   Aula 23 - Acessando Banco de Dados mongo BD com Python
from pymongo import collection


def get_database():
    from pymongo import MongoClient

    # import pymongo

    CONNECTION_STRING = (
        "mongodb+srv://root:<WGRHIth3BzcSS4z1>@cluster0.tnzynwo.mongodb.net/"
    )
    client = MongoClient(CONNECTION_STRING)
    print("Conectado com sucesso!")
    return client["sample_airbnb"]


get_database()
