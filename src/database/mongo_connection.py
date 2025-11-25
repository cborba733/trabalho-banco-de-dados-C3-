from pymongo import MongoClient

class MongoConnection:
    def __init__(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client["petshop"]
            print("[OK] Conectado ao MongoDB com sucesso!")
        except Exception as e:
            print(f"[ERRO] Falha ao conectar ao MongoDB: {e}")
            self.client = None
            self.db = None

    def get_collection(self, name):
        if self.db is not None:
            return self.db[name]
        else:
            print("[ERRO] Banco de dados não inicializado!")
            return None

mongo_connection = MongoConnection()
