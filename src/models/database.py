from pymongo import MongoClient

#fallos en la conexion 
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

#agregar la uri de la conexion a la base de datos de mongo 
MONGO_URI = "mongodb+srv://canteroalejandra28_db_user:P73R3WVZoT5mXlwh@cluster0.m7cuslt.mongodb.net/?appName=Cluster0" \

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000) # tiempo de espera de 5 segundos 

db = client.dataap
collection = db.trainee

try:
    client.server_info()
    client.admin.command("ping")
    print("conexion exitosa a mongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"error al conectar a mongoDB: {e}")
finally:
    client.close()
