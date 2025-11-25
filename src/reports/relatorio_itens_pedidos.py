from bson import ObjectId
from database.mongo_connection import mongo_connection

class RelatorioItensPedidos:

    def __init__(self):
        self.itens = mongo_connection.get_collection("itens_pedidos")
        self.clientes = mongo_connection.get_collection("clientes")
        self.produtos = mongo_connection.get_collection("produtos")
        self.pedidos = mongo_connection.get_collection("pedidos")

    def gerar(self):
        print("\n=== RELATÓRIO: ITENS DOS PEDIDOS (JUNÇÃO) ===\n")

        # Cabeçalho da tabela
        print("+----------------------+----------------------+--------------+--------------+----------------------+")
        print("| {:20} | {:20} | {:10} | {:10} | {:20} |".format(
            "Cliente", "Produto", "Qtd", "Subtotal", "ID Pedido"
        ))
        print("+----------------------+----------------------+--------------+--------------+----------------------+")

        # Percorrer todos os itens
        for item in self.itens.find():

            pedido = self.pedidos.find_one({"_id": item["pedido_id"]})
            cliente = self.clientes.find_one({"_id": pedido["cliente_id"]}) if pedido else None
            produto = self.produtos.find_one({"_id": item["produto_id"]})

            nome_cliente = cliente["nome"] if cliente else "Desconhecido"
            nome_produto = produto["nome"] if produto else "Desconhecido"

            print("| {:20} | {:20} | {:10} | {:10.2f} | {:20} |".format(
                nome_cliente,
                nome_produto,
                item["quantidade"],
                item["subtotal"],
                str(item["pedido_id"])
            ))

        print("+----------------------+----------------------+--------------+--------------+----------------------+\n")
