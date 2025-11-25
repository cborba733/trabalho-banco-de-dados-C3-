from database.mongo_connection import mongo_connection

class RelatorioPedidos:

    def __init__(self):
        self.collection = mongo_connection.get_collection("pedidos")

    def gerar(self):
        print("\n=== RELATÓRIO DE PEDIDOS ===")
        pedidos = self.collection.find()

        for p in pedidos:
            print(
                f"ID: {p['_id']} | Cliente: {p['cliente_id']} | Data: {p['data']} | Total: {p['total']}"
            )

        print("\nTotal de pedidos:", self.collection.count_documents({}))
        print("================================\n")
