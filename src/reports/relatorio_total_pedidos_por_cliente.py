from database.mongo_connection import mongo_connection

class RelatorioTotalPedidosPorCliente:

    def __init__(self):
        self.clientes = mongo_connection.get_collection("clientes")
        self.pedidos = mongo_connection.get_collection("pedidos")

    def gerar(self):
        print("\n===== RELATÓRIO: TOTAL DE PEDIDOS POR CLIENTE =====\n")

        print("---------------------------------------------------------------")
        print(f"{'Cliente':25} | {'Pedidos':7} | {'Valor Total'}")
        print("---------------------------------------------------------------")

        # Lista todos os clientes (inclusive os que nunca pediram)
        for cliente in self.clientes.find():

            pedidos_cliente = list(
                self.pedidos.find({"cliente_id": cliente["_id"]})
            )

            qtd = len(pedidos_cliente)
            total = sum(p.get("total", 0) for p in pedidos_cliente)

            print(f"{cliente['nome'][:25]:25} | {qtd:^7} | R${total:,.2f}")

        print("---------------------------------------------------------------\n")
