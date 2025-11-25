from controllers.clientes_controller import ClientesController
from controllers.produtos_controller import ProdutosController
from controllers.pedidos_controller import PedidosController
from controllers.itens_pedidos_controller import ItensPedidosController

from reports.relatorio_total_pedidos_por_cliente import RelatorioTotalPedidosPorCliente
from reports.relatorio_itens_com_cliente_produto import RelatorioItensClienteProduto


def menu_principal():
    while True:
        print("\n=====================================")
        print(" SISTEMA DE VENDAS - PET SHOP AMIGO CACHORRO")
        print(" Desenvolvido por: Caio Borba da Silva Souza")
        print("=====================================")

        print("\n=== MENU PRINCIPAL ===")
        print("1 - Clientes")
        print("2 - Produtos")
        print("3 - Pedidos")
        print("4 - Itens dos Pedidos")
        print("5 - Relatórios")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "3":
            menu_pedidos()
        elif opcao == "4":
            menu_itens_pedidos()
        elif opcao == "5":
            menu_relatorios()
        elif opcao == "0":
            print("\nSaindo do sistema...\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


# ========================= CLIENTES ============================
def menu_clientes():
    controller = ClientesController()

    while True:
        print("\n=== MENU CLIENTES ===")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.inserir()
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            controller.atualizar()
        elif opcao == "4":
            controller.remover()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ========================= PRODUTOS ============================
def menu_produtos():
    controller = ProdutosController()

    while True:
        print("\n=== MENU PRODUTOS ===")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.inserir()
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            controller.atualizar()
        elif opcao == "4":
            controller.remover()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ========================= PEDIDOS ============================
def menu_pedidos():
    controller = PedidosController()

    while True:
        print("\n=== MENU PEDIDOS ===")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.inserir()
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            controller.atualizar()
        elif opcao == "4":
            controller.remover()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ========================= ITENS DOS PEDIDOS ============================
def menu_itens_pedidos():
    controller = ItensPedidosController()

    while True:
        print("\n=== MENU ITENS DOS PEDIDOS ===")
        print("1 - Inserir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            controller.inserir()
        elif opcao == "2":
            controller.listar()
        elif opcao == "3":
            controller.atualizar()
        elif opcao == "4":
            controller.remover()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ========================= RELATÓRIOS ============================
def menu_relatorios():
    rel1 = RelatorioTotalPedidosPorCliente()
    rel2 = RelatorioItensClienteProduto()

    while True:
        print("\n=== RELATÓRIOS ===")
        print("1 - Total de pedidos por cliente (agrupamento)")
        print("2 - Itens pedidos + cliente + produto (junção)")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            rel1.gerar()
        elif opcao == "2":
            rel2.gerar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


# ========================= MAIN ============================
if __name__ == "__main__":
    menu_principal()
