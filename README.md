🐾 Trabalho C3 – Banco de Dados Não Relacional (MongoDB)
Pet Shop Amigo Cachorro – Sistema de Vendas
Aluno: Caio Borba da Silva Souza
Disciplina: Banco de Dados Não Relacional
Docente: Howard Cruz Roatti

📌 Sobre o Projeto
Este repositório contém o projeto do C3, uma evolução direta do C2, migrando o sistema do Pet Shop Amigo Cachorro para o MongoDB, utilizando Python e Pymongo.

O sistema permite:

Cadastro de clientes

Cadastro de produtos

Cadastro de pedidos

Itens dentro dos pedidos

Relatórios completos

Persistência real no MongoDB

Organização em camadas (controllers, database, reports, migrate)

🎥 Vídeo de Demonstração (C3)
👉 https://youtu.be/HW-ggNEzDdE

O vídeo demonstra:

✔ CRUD de todas as entidades
✔ MongoDB funcionando após conexão
✔ Relatórios exigidos no edital
✔ Sistema rodando no terminal
✔ Menu 100% funcional
✔ Funcionamento completo da aplicação

🛠️ Tecnologias Utilizadas
Python 3.12

MongoDB Community Server

Pymongo

Ambiente virtual (venv)

Linux + Terminal

📂 Estrutura do Projeto (REAL da VM /C3/src)
src/
├── controllers/
│   ├── clientes_controller.py
│   ├── produtos_controller.py
│   ├── pedidos_controller.py
│   └── itens_pedidos_controller.py
│
├── database/
│   └── mongo_connection.py
│
├── migrate/
│   └── migrate_all.py     ← (NOVIDADE)
│
├── reports/
│   ├── relatorio_total_pedidos_por_cliente.py
│   └── relatorio_itens_com_cliente_produto.py
│
├── main.py
├── diagrama.pdf           ← (Exigência do edital)
└── (venv/)                ← (não enviado ao GitHub)
✔ A pasta migrate/ agora faz parte oficial da entrega
✔ O arquivo migrate_all.py realiza a migração C2 → C3 (PostgreSQL → MongoDB)

⚙️ Como Executar o Sistema
1️⃣ Criar ambiente virtual
python3 -m venv venv
2️⃣ Ativar ambiente
source venv/bin/activate
3️⃣ Instalar dependências
pip install pymongo psycopg2-binary
4️⃣ Iniciar o MongoDB
sudo systemctl start mongod
5️⃣ Executar o sistema
python3 main.py
🔄 Migração do C2 (PostgreSQL) → C3 (MongoDB)
A pasta /migrate contém o arquivo:

migrate_all.py
Ele migra:

clientes

produtos

pedidos

itens dos pedidos

para dentro do banco petshop no MongoDB.

Para rodar a migração:
cd ~/C3/src/migrate
python3 migrate_all.py

📊 Relatórios Implementados (conforme edital)

1 – Total de pedidos por cliente (Agrupamento)
Exibe:

Nome do cliente

Quantidade de pedidos

Valor total gasto

Inclui clientes sem pedidos

2 – Itens pedidos com cliente e produto (Junção)
Exibe:

Cliente

Produto

Quantidade

Subtotal

ID do pedido

📐 Diagrama (Exigência do Edital)

O diagrama relacional utilizado como base está em:


/C3/src/diagrama.pdf
✔️ Conclusão
Este projeto atende 100% das exigências do C3, incluindo:

✔ Banco Não Relacional (MongoDB)
✔ CRUD completo
✔ Relatórios obrigatórios
✔ Vídeo demonstrativo
✔ Estrutura organizada
✔ Diagrama incluído
✔ Script de migração completo
✔ Repositório limpo e bem estruturado

