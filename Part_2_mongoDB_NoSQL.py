import pymongo

# Conectando ao MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["bank"]

# Inserindo documentos
documento1 = {"cliente": "João", "saldo": 1000}
documento2 = {"cliente": "Maria", "saldo": 500}

collection.insert_many([documento1, documento2])

# Recuperando informações
for documento in collection.find():
    print(documento)
