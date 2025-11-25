from bson import ObjectId
from database.mongo_connection import mongo_connection

class RelatorioItensClienteProduto:

    def __init__(self):
        self.itens = mongo_connection.get_collection("itens_pedidos")
        self.pedidos = mongo_connection.get_collection("pedidos")
        self.clientes = mongo_connection.get_collection("clientes")
        self.produtos = mongo_connection.get_collection("produtos")

    def gerar(self):
        print("\n=== RELATÓRIO: ITENS COM CLIENTE E PRODUTO ===\n")

        # Cabeçalho da tabela
        print(f"{'Cliente':<20} {'Produto':<20} {'Qtd':<5} {'Subtotal (R$)':<15}")

        print("-" * 60)

        for item in self.itens.find():

            produto = self.produtos.find_one({"_id": item["produto_id"]})
            pedido = self.pedidos.find_one({"_id": item["pedido_id"]})

            if not produto or not pedido:
                continue

            cliente = self.clientes.find_one({"_id": pedido["cliente_id"]})
            nome_cliente = cliente["nome"] if cliente else "Desconhecido"

            print(
                f"{nome_cliente:<20} "
                f"{produto['nome']:<20} "
                f"{item['quantidade']:<5} "
                f"{item['subtotal']:<15.2f}"
            )
