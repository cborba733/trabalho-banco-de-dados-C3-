class Pedido:
    def __init__(self, cliente_id, data, total):
        self.cliente_id = cliente_id
        self.data = data
        self.total = total

    def to_dict(self):
        return {
            "cliente_id": self.cliente_id,
            "data": self.data,
            "total": self.total
        }
