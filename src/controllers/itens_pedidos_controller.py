from bson import ObjectId
from database.mongo_connection import mongo_connection


class ItensPedidosController:

    def __init__(self):
        self.collection = mongo_connection.get_collection("itens_pedidos")
        self.produtos = mongo_connection.get_collection("produtos")
        self.pedidos = mongo_connection.get_collection("pedidos")

    def inserir(self):
        print("\n--- CADASTRAR ITEM DO PEDIDO ---")

        pedido_id = input("ID do pedido: ")

        try:
            pedido = self.pedidos.find_one({"_id": ObjectId(pedido_id)})
        except:
            print("ID do pedido inválido!")
            return

        if not pedido:
            print("Pedido não encontrado!")
            return

        produto_id = input("ID do produto: ")

        try:
            produto = self.produtos.find_one({"_id": ObjectId(produto_id)})
        except:
            print("ID do produto inválido!")
            return

        if not produto:
            print("Produto não encontrado!")
            return

        quantidade = int(input("Quantidade: "))
        subtotal = float(produto["preco"]) * quantidade

        item = {
            "pedido_id": ObjectId(pedido_id),
            "produto_id": ObjectId(produto_id),
            "quantidade": quantidade,
            "subtotal": subtotal
        }

        self.collection.insert_one(item)

        novo_total = pedido.get("total", 0.0) + subtotal

        self.pedidos.update_one(
            {"_id": ObjectId(pedido_id)},
            {"$set": {"total": novo_total}}
        )

        print("[OK] Item inserido!")

    def listar(self):
        print("\n--- LISTA DE ITENS DO PEDIDO ---\n")

        for item in self.collection.find():

            produto = self.produtos.find_one({"_id": item["produto_id"]})
            nome_produto = produto["nome"] if produto else "Desconhecido"

            print(
                f"ID Item: {item['_id']} | "
                f"Produto: {nome_produto} | "
                f"Pedido: {item['pedido_id']} | "
                f"Quantidade: {item['quantidade']} | "
                f"Subtotal: R${item['subtotal']:.2f}"
            )

    def atualizar(self):
        item_id = input("ID do item: ")

        try:
            item = self.collection.find_one({"_id": ObjectId(item_id)})
        except:
            print("ID inválido!")
            return

        if not item:
            print("Item não encontrado!")
            return

        quantidade = int(input("Nova quantidade: "))

        produto = self.produtos.find_one({"_id": item["produto_id"]})

        novo_subtotal = produto["preco"] * quantidade
        diferenca = novo_subtotal - item["subtotal"]

        self.collection.update_one(
            {"_id": ObjectId(item_id)},
            {"$set": {"quantidade": quantidade, "subtotal": novo_subtotal}}
        )

        self.pedidos.update_one(
            {"_id": item["pedido_id"]},
            {"$inc": {"total": diferenca}}
        )

        print("[OK] Item atualizado!")

    def remover(self):
        item_id = input("ID do item: ")

        try:
            item = self.collection.find_one({"_id": ObjectId(item_id)})
        except:
            print("ID inválido!")
            return

        if not item:
            print("Item não encontrado!")
            return

        self.collection.delete_one({"_id": ObjectId(item_id)})

        self.pedidos.update_one(
            {"_id": item["pedido_id"]},
            {"$inc": {"total": -item["subtotal"]}}
        )

        print("[OK] Item removido!\n")
