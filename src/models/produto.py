from bson import ObjectId

class Produto:
    def __init__(self, nome, descricao, preco, estoque, _id=None):
        self._id = ObjectId(_id) if _id else None
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def to_dict(self):
        d = {
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque
        }
        if self._id:
            d["_id"] = self._id
        return d

    @staticmethod
    def from_dict(d):
        return Produto(
            nome=d.get("nome", ""),
            descricao=d.get("descricao", ""),
            preco=d.get("preco", 0.0),
            estoque=d.get("estoque", 0),
            _id=str(d.get("_id")) if d.get("_id") else None
        )
