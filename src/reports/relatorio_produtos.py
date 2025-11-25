from database.mongo_connection import mongo_connection

class RelatorioProdutos:
    def __init__(self):
        self.collection = mongo_connection.get_collection("produtos")

    def gerar(self):
        print("\n=== RELATÓRIO DE PRODUTOS ===")
        produtos = self.collection.find()
        total = 0

        for p in produtos:
            print(
                f"ID: {p.get('_id')} | Nome: {p.get('nome')} | Descrição: {p.get('descricao')} | "
                f"Preço: {p.get('preco')} | Estoque: {p.get('estoque')}"
            )
            total += 1

        print("\nTotal de produtos:", total)
        print("==============================\n")
