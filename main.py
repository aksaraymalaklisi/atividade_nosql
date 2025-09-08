from settings import DatabaseSettings
from pymongo import MongoClient

dbConfig = DatabaseSettings()

client = MongoClient(dbConfig.uri)
db = client[dbConfig.database]
collection = db[dbConfig.collection]


"""
O objetivo é criar um CRUD simples com Pymongo.
Há 4 métodos do MongoClient que permite manipular a collection:

insert_one(documento) - Recebe um documento (dict) e insere-o na database.
Obs.: Esse método também retorna o ID do documento criado.

find_one(filter, projection=None) - Recebe um documento (dict) que é utilizado como filtro de busca.
Obs.: projection, por padrão, está vazio. Ele define que campos serão retornados usando booleanos. Ex.: {"nome":1, "idade":False}

update_one(filter, update, upsert=False) - Recebe um dict como filtro de busca e, no segundo argumento, um dict contendo a mudança requisitada.
Obs.: O segundo argumento DEVE CONTER UM OPERADOR do MongoDB. Ex.: {"$set": {"nome":"Carlos"}}.
        Já o upsert, se for verdadeiro (falso por padrão), irá INSERIR o documento usando o filter como base SE o documento procurado
        não existir.
        Ele também retorna um objeto chamado (UpdateResult). Ele possui alguns atributos úteis, como matched_count, modified_count.
        Se você usou o upsert, ele também manda o id do documento adicionado no atributo upserted_id.

delete_one(filter) - Similar ao find_one, mas APAGA o documento encontrado.
Obs.: Ele retorna um objeto chamado DeleteResult. Ele possui um atributo chamado deleted_count.
"""