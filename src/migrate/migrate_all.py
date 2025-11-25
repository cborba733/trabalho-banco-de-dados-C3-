import psycopg2
from pymongo import MongoClient

# ===============================
#   MIGRAÇÃO C2 → C3
#   PostgreSQL → MongoDB
# ===============================

def conectar_postgres():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="lab@Database2025",   # << SENHA CORRETA
        host="localhost",
        port="5432"
    )

def conectar_mongo():
    mongo = MongoClient("mongodb://localhost:27017/")
    return mongo["petshop"]   # banco da C3


# ===============================
#   CLIENTES
# ===============================

def migrate_clientes(db_mongo):
    conn = conectar_postgres()
    cur = conn.cursor()

    print("\n[CLIENTES] Migrando clientes...")

    cur.execute("""
        SELECT id_cliente, nome, email, telefone, endereco
        FROM clientes
    """)

    rows = cur.fetchall()
    documentos = []

    for r in rows:
        documentos.append({
            "_id": r[0],
            "nome": r[1],
            "email": r[2],
            "telefone": r[3],
            "endereco": r[4]
        })

    if documentos:
        db_mongo["clientes"].insert_many(documentos)

    print(f"[CLIENTES] {len(documentos)} registros migrados.")

    cur.close()
    conn.close()



# ===============================
#   PRODUTOS
# ===============================

def migrate_produtos(db_mongo):
    conn = conectar_postgres()
    cur = conn.cursor()

    print("\n[PRODUTOS] Migrando produtos...")

    cur.execute("""
        SELECT id_produto, nome, descricao, preco, estoque
        FROM produtos
    """)

    rows = cur.fetchall()
    documentos = []

    for r in rows:
        documentos.append({
            "_id": r[0],
            "nome": r[1],
            "descricao": r[2],
            "preco": float(r[3]),
            "estoque": r[4]
        })

    if documentos:
        db_mongo["produtos"].insert_many(documentos)

    print(f"[PRODUTOS] {len(documentos)} registros migrados.")

    cur.close()
    conn.close()



# ===============================
#   PEDIDOS
# ===============================

def migrate_pedidos(db_mongo):
    conn = conectar_postgres()
    cur = conn.cursor()

    print("\n[PEDIDOS] Migrando pedidos...")

    cur.execute("""
        SELECT id_pedido, id_item_pedido, id_cliente, data_pedido, total, status
        FROM pedidos
    """)

    rows = cur.fetchall()
    documentos = []

    for r in rows:
        documentos.append({
            "_id": r[0],
            "id_item_pedido": r[1],    # << MANTENDO DO JEITO DO SEU DIAGRAMA
            "id_cliente": r[2],
            "data_pedido": str(r[3]),
            "total": float(r[4]),
            "status": r[5]
        })

    if documentos:
        db_mongo["pedidos"].insert_many(documentos)

    print(f"[PEDIDOS] {len(documentos)} registros migrados.")

    cur.close()
    conn.close()



# ===============================
#   ITENS_PEDIDOS
# ===============================

def migrate_itens_pedidos(db_mongo):
    conn = conectar_postgres()
    cur = conn.cursor()

    print("\n[ITENS_PEDIDOS] Migrando itens dos pedidos...")

    cur.execute("""
        SELECT id_item_pedido, id_produto, id_pedido, quantidade, subtotal
        FROM itens_pedidos
    """)

    rows = cur.fetchall()
    documentos = []

    for r in rows:
        documentos.append({
            "_id": r[0],
            "id_produto": r[1],
            "id_pedido": r[2],
            "quantidade": r[3],
            "subtotal": float(r[4])
        })

    if documentos:
        db_mongo["itens_pedidos"].insert_many(documentos)

    print(f"[ITENS_PEDIDOS] {len(documentos)} registros migrados.")

    cur.close()
    conn.close()



# ===============================
#   EXECUTAR TUDO
# ===============================

if __name__ == "__main__":
    print("\n===== MIGRAÇÃO COMPLETA C2 → C3 =====")

    db_mongo = conectar_mongo()

    migrate_clientes(db_mongo)
    migrate_produtos(db_mongo)
    migrate_pedidos(db_mongo)
    migrate_itens_pedidos(db_mongo)

    print("\n===== MIGRAÇÃO FINALIZADA COM SUCESSO =====\n")
