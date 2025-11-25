from bson import ObjectId
from models.cliente import Cliente
from database.mongo_connection import mongo_connection

class ClientesController:
    def __init__(self):
        self.collection = mongo_connection.get_collection("clientes")

    def inserir(self):
        nome = input("Nome do cliente: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        endereco = input("Endereço: ")

        cliente = Cliente(nome, email, telefone, endereco)
        # insere e pega o _id gerado
        result = self.collection.insert_one(cliente.to_dict())
        print("\n[OK] Cliente cadastrado! ID:", result.inserted_id, "\n")

    def listar(self):
        print("\n--- LISTA DE CLIENTES ---")
        cursor = self.collection.find()
        count = 0
        for c in cursor:
            # imprime todos os campos, inclusive endereço e email
            print(f"ID: {c.get('_id')} | Nome: {c.get('nome')} | Email: {c.get('email')} | Telefone: {c.get('telefone')} | Endereço: {c.get('endereco')}")
            count += 1
        if count == 0:
            print("(Nenhum cliente cadastrado)")
        print()

    def atualizar(self):
        _id = input("ID do cliente que deseja atualizar: ")
        try:
            obj_id = ObjectId(_id)
        except Exception:
            print("[ERRO] ID inválido.")
            return

        # ler dados novos
        nome = input("Novo nome (deixe vazio para manter): ")
        email = input("Novo email (deixe vazio para manter): ")
        telefone = input("Novo telefone (deixe vazio para manter): ")
        endereco = input("Novo endereço (deixe vazio para manter): ")

        # montar dict só com campos preenchidos
        update_fields = {}
        if nome:
            update_fields["nome"] = nome
        if email:
            update_fields["email"] = email
        if telefone:
            update_fields["telefone"] = telefone
        if endereco:
            update_fields["endereco"] = endereco

        if not update_fields:
            print("[AVISO] Nada para atualizar.")
            return

        result = self.collection.update_one({"_id": obj_id}, {"$set": update_fields})
        if result.matched_count:
            print("\n[OK] Cliente atualizado!\n")
        else:
            print("\n[ERRO] Cliente não encontrado.\n")

    def remover(self):
        _id = input("ID do cliente que deseja remover: ")
        try:
            obj_id = ObjectId(_id)
        except Exception:
            print("[ERRO] ID inválido.")
            return

        confirm = input("Tem certeza que deseja remover esse cliente? (s/N): ")
        if confirm.lower() != "s":
            print("Operação cancelada.")
            return

        result = self.collection.delete_one({"_id": obj_id})
        if result.deleted_count:
            print("\n[OK] Cliente removido!\n")
        else:
            print("\n[ERRO] Cliente não encontrado.\n")
