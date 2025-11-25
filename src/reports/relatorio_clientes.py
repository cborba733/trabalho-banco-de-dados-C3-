from database.mongo_connection import mongo_connection

class RelatorioClientes:

    def __init__(self):
        self.clientes = mongo_connection.get_collection("clientes")
        self.pedidos = mongo_connection.get_collection("pedidos")

    def gerar(self):
        print("\n=== RELATÓRIO: TOTAL DE PEDIDOS POR CLIENTE ===\n")

        # Buscar todos os clientes
        lista_clientes = list(self.clientes.find())

        # Cabeçalho da tabela
        print("+----------------------+----------------------+----------------------+")
        print("| {:20} | {:20} | {:20} |".format(
            "Cliente", "Qtde Pedidos", "Total (R$)"
        ))
        print("+----------------------+----------------------+----------------------+")

        for cliente in lista_clientes:

            # Buscar pedidos do cliente
            pedidos_cliente = list(self.pedidos.find({"cliente_id": cliente["_id"]}))

            qtd_pedidos = len(pedidos_cliente)
            total = sum(p.get("total", 0.0) for p in pedidos_cliente)

            print("| {:20} | {:20} | {:20.2f} |".format(
                cliente["nome"],
                qtd_pedidos,
                total
            ))

        print("+----------------------+----------------------+----------------------+\n")
