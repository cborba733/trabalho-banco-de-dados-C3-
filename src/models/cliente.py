from bson import ObjectId

class Cliente:
    def __init__(self, nome, email, telefone, endereco, _id=None):
        # _id é opcional: normalmente deixamos o Mongo gerar ObjectId automaticamente
        self._id = ObjectId(_id) if _id else None
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def to_dict(self):
        d = {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco
        }
        # só incluir _id se existir (para update por exemplo)
        if self._id is not None:
            d["_id"] = self._id
        return d

    @staticmethod
    def from_dict(d):
        # cria objeto a partir de documento Mongo
        _id = d.get("_id")
        return Cliente(
            nome=d.get("nome", ""),
            email=d.get("email", ""),
            telefone=d.get("telefone", ""),
            endereco=d.get("endereco", ""),
            _id=str(_id) if _id is not None else None
        )
