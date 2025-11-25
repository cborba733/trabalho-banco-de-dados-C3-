from bson import ObjectId
from database.mongo_connection import mongo_connection

class PedidosController:

    def __init__(self):
        self.collection = mongo_connection.get_collection("pedidos")
        self.clientes = mongo_connection.get_collection("clientes")

    # =============== INSERIR PEDIDO =====================
    def inserir(self):
        print("\n--- CADASTRAR PEDIDO ---")

        cliente_id = input("ID do cliente: ")

        try:
            cliente = self.clientes.find_one({"_id": ObjectId(cliente_id)})
        except:
            print("ID de cliente inválido!")
            return

        if not cliente:
            print("Cliente não encontrado!")
            return

        pedido = {
            "cliente_id": ObjectId(cliente_id),
            "data": input("Data (DD/MM/AAAA): "),
            "status": input("Status (pago/pendente/nao pago): ").lower(),
            "total": 0.0
        }

        result = self.collection.insert_one(pedido)
        print(f"[OK] Pedido criado! ID: {result.inserted_id}\n")

    # =============== LISTAR PEDIDOS =====================
    def listar(self):
        print("\n--- LISTA DE PEDIDOS ---\n")

        for p in self.collection.find():

            cliente = self.clientes.find_one({"_id": p["cliente_id"]})
            nome_cliente = cliente["nome"] if cliente else "Desconhecido"

            # corrige pedidos antigos sem o campo "total"
            total = p.get("total", 0.0)
            data = p.get("data", "---")
            status = p.get("status", "indefinido")

            print(
                f"ID: {p['_id']} | "
                f"Cliente: {nome_cliente} | "
                f"Data: {data} | "
                f"Total: R${total:.2f} | "
                f"Status: {status}"
            )

    # =============== ATUALIZAR PEDIDO =====================
    def atualizar(self):
        pedido_id = input("ID do pedido: ")

        try:
            pedido = self.collection.find_one({"_id": ObjectId(pedido_id)})
        except:
            print("ID inválido!")
            return

        if not pedido:
            print("Pedido não encontrado!")
            return

        while True:
            print("\n--- CAMPOS QUE VOCÊ PODE ATUALIZAR ---")
            print("1 - Alterar cliente")
            print("2 - Alterar data")
            print("3 - Alterar status")
            print("4 - Alterar total")
            print("0 - Voltar")

            opc = input("Escolha: ")

            if opc == "1":
                novo_cliente = input("Novo ID de cliente: ")
                try:
                    cliente = self.clientes.find_one({"_id": ObjectId(novo_cliente)})
                    if cliente:
                        self.collection.update_one(
                            {"_id": ObjectId(pedido_id)},
                            {"$set": {"cliente_id": ObjectId(novo_cliente)}}
                        )
                        print("[OK] Cliente atualizado!")
                    else:
                        print("Cliente não encontrado!")
                except:
                    print("ID inválido!")

            elif opc == "2":
                nova_data = input("Nova data (DD/MM/AAAA): ")
                self.collection.update_one(
                    {"_id": ObjectId(pedido_id)},
                    {"$set": {"data": nova_data}}
                )
                print("[OK] Data atualizada!")

            elif opc == "3":
                novo_status = input("Novo status: ")
                self.collection.update_one(
                    {"_id": ObjectId(pedido_id)},
                    {"$set": {"status": novo_status}}
                )
                print("[OK] Status atualizado!")

            elif opc == "4":
                try:
                    novo_total_input = input("Novo total (ex: 150.00): ").strip()
                    novo_total = float(novo_total_input)
                except:
                    print("Valor inválido! Informe um número (ex: 150.00).")
                    continue

                self.collection.update_one(
                    {"_id": ObjectId(pedido_id)},
                    {"$set": {"total": novo_total}}
                )
                print("[OK] Total atualizado!")

            elif opc == "0":
                break

            else:
                print("Opção inválida!")

    # =============== REMOVER PEDIDO =====================
    def remover(self):
        pedido_id = input("ID do pedido: ")

        try:
            self.collection.delete_one({"_id": ObjectId(pedido_id)})
        except:
            print("ID inválido!")
            return

        print("[OK] Pedido removido!\n")

