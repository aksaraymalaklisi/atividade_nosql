from settings import DatabaseSettings
from pymongo import MongoClient

dbConfig = DatabaseSettings()

client = MongoClient(dbConfig.uri)
db = client[dbConfig.database]
collection = db[dbConfig.collection]


def create_one(doc):
    if doc:
        return collection.insert_one(doc)
    else:
        print("Erro.")

def read_one(keydoc):
    if keydoc:
        return collection.find_one(keydoc)
    else:
        print("Erro.")

def update_one(keydoc, newdoc):
    if keydoc and newdoc:
            set_operator = {"$set": newdoc}
            return collection.update_one(keydoc, set_operator)
    else:
        print('Erro.')

def delete_one(keydoc):
    if keydoc:
        return collection.delete_one(keydoc)
    else:
        print('Erro.')
        
# CREATE
print(create_one({"nome":"Carlos", "idade":"34"}))

# READ
print(read_one({"nome":"Carlos"}))

# UPDATE
print(update_one({"nome":"Carlos"}, {"idade":35}))

# DELETE
print(delete_one({"nome":"Carlos"}))