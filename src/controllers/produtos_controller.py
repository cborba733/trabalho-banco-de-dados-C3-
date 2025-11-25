from bson import ObjectId
from models.produto import Produto
from database.mongo_connection import mongo_connection

class ProdutosController:
    def __init__(self):
        self.collection = mongo_connection.get_collection("produtos")

    def inserir(self):
        print("\n--- CADASTRAR PRODUTO ---")
        nome = input("Nome do produto: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque inicial: "))

        produto = Produto(nome, descricao, preco, estoque)
        result = self.collection.insert_one(produto.to_dict())

        print("\n[OK] Produto cadastrado! ID:", result.inserted_id)

    def listar(self):
        print("\n--- LISTA DE PRODUTOS ---")
        produtos = self.collection.find()
        count = 0
        for p in produtos:
            print(
                f"ID: {p.get('_id')} | Nome: {p.get('nome')} | Descrição: {p.get('descricao')} | "
                f"Preço: {p.get('preco')} | Estoque: {p.get('estoque')}"
            )
            count += 1

        if count == 0:
            print("(Nenhum produto cadastrado)")
        print()

    def atualizar(self):
        _id = input("ID do produto que deseja atualizar: ")
        try:
            obj_id = ObjectId(_id)
        except:
            print("[ERRO] ID inválido.")
            return

        nome = input("Novo nome (vazio para manter): ")
        descricao = input("Nova descrição (vazio para manter): ")
        preco = input("Novo preço (vazio para manter): ")
        estoque = input("Novo estoque (vazio para manter): ")

        update = {}

        if nome:
            update["nome"] = nome
        if descricao:
            update["descricao"] = descricao
        if preco:
            update["preco"] = float(preco)
        if estoque:
            update["estoque"] = int(estoque)

        if not update:
            print("[AVISO] Nada para atualizar.")
            return

        result = self.collection.update_one({"_id": obj_id}, {"$set": update})

        if result.matched_count:
            print("\n[OK] Produto atualizado!")
        else:
            print("\n[ERRO] Produto não encontrado.")

    def remover(self):
        _id = input("ID do produto que deseja remover: ")
        try:
            obj_id = ObjectId(_id)
        except:
            print("[ERRO] ID inválido.")
            return

        confirm = input("Tem certeza que deseja remover este produto? (s/N): ")
        if confirm.lower() != "s":
            print("Cancelado.")
            return

        result = self.collection.delete_one({"_id": obj_id})

        if result.deleted_count:
            print("\n[OK] Produto removido!")
        else:
            print("\n[ERRO] Produto não encontrado.")
