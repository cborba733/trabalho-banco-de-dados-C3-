class ItemPedido:
    def __init__(self, pedido_id, produto_id, quantidade, subtotal):
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.subtotal = subtotal

    def to_dict(self):
        return {
            "pedido_id": self.pedido_id,
            "produto_id": self.produto_id,
            "quantidade": self.quantidade,
            "subtotal": self.subtotal
        }
