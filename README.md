🐾 Trabalho C3 – Banco de Dados Não Relacional (MongoDB)
Pet Shop Amigo Cachorro – Sistema de Vendas

Aluno: Caio Borba da Silva Souza
Disciplina: Banco de Dados Não Relacional
Docente: Howard Cruz Roatti

📌 Sobre o Projeto

Este repositório contém o projeto da C3, uma evolução da C2, migrando o sistema do Pet Shop Amigo Cachorro para o MongoDB, utilizando Python e Pymongo.

O sistema permite:

Cadastro de clientes

Cadastro de produtos

Cadastro de pedidos

Itens dentro dos pedidos

Relatórios completos

Persistência real em MongoDB

🎥 Vídeo de Demonstração (C3)

👉 https://youtu.be/HW-ggNEzDdE

O vídeo demonstra:

✔ CRUD de todas as entidades
✔ MongoDB funcionando
✔ Relatórios exigidos no edital
✔ Sistema rodando no terminal
✔ Estrutura organizada do projeto

🛠️ Tecnologias Utilizadas

Python 3.12

MongoDB Community Server

Pymongo

Virtualenv

Linux + Terminal

📂 Estrutura Real do Projeto

Esta é a estrutura EXATA da  pasta /C3/src dentro da VM:

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
├── reports/
│   ├── relatorio_total_pedidos_por_cliente.py
│   └── relatorio_itens_com_cliente_produto.py
│
├── main.py
├── diagrama.pdf
└── venv/   (ambiente virtual - não enviado ao GitHub)


(As pastas models, utils, migrate não são utilizadas nesta versão do sistema e foram removidas do README para refletir a entrega real.)

⚙️ Como Executar
1️⃣ Criar ambiente virtual
python3 -m venv venv

2️⃣ Ativar ambiente
source venv/bin/activate

3️⃣ Instalar dependências
pip install pymongo

4️⃣ Iniciar o MongoDB
sudo systemctl start mongod

5️⃣ Executar o sistema
python3 main.py

📊 Relatórios Implementados (conforme edital)
1 – Total de pedidos por cliente (Agrupamento)

Exibe:

Cliente

Quantidade de pedidos

Valor total gasto

Inclui clientes sem pedidos

2 – Itens pedidos com cliente e produtos (Junção)

Exibe:

Nome do cliente

Nome do produto

Quantidade

Subtotal

ID do pedido

📐 Diagrama (Exigência do Edital)

O diagrama encontra-se em:

/C3/src/diagrama.pdf

✔️ Conclusão

Este sistema atende todas as exigências da C3, incluindo:

✔ Banco Não Relacional (MongoDB)
✔ CRUD completo
✔ Relatórios obrigatórios
✔ Vídeo demonstrativo
✔ Estrutura organizada
✔ Diagrama incluído
✔ Repositório limpo e adequado ao edital
