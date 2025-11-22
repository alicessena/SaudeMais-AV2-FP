# crud_farmacia.py
from utils import buscar_por_id, gerar_novo_id

def menu_farmacia(lista_farmacia):
    while True:
        print("\n--- GESTÃO DE FARMÁCIA ---")
        print("1. Solicitar/Cadastrar Remédio (Entrada)")
        print("2. Consultar Estoque")
        print("3. Registrar Retirada (Saída)")
        print("4. Remover Remédio do Sistema")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome do Remédio: ")
            qtd = int(input("Quantidade a adicionar: "))
            
            # Verifica se já existe para somar
            existente = next((r for r in lista_farmacia if r['nome'].lower() == nome.lower()), None)
            if existente:
                existente['qtd'] += qtd
                print(f"Estoque atualizado: {existente['qtd']}")
            else:
                novo_id = gerar_novo_id(lista_farmacia)
                remedio = {'id': novo_id, 'nome': nome, 'qtd': qtd}
                lista_farmacia.append(remedio)
                print("Remédio cadastrado.")

        elif opcao == '2':
            print("\nEstoque:")
            for r in lista_farmacia:
                print(f"ID: {r['id']} | Nome: {r['nome']} | Qtd: {r['qtd']}")

        elif opcao == '3':
            r_id = int(input("ID do Remédio: "))
            qtd_saida = int(input("Quantidade retirada: "))
            r = buscar_por_id(lista_farmacia, r_id)
            if r:
                if r['qtd'] >= qtd_saida:
                    r['qtd'] -= qtd_saida
                    print(f"Retirada efetuada. Restam: {r['qtd']}")
                else:
                    print("Estoque insuficiente.")
            else:
                print("Remédio não encontrado.")

        elif opcao == '4':
            r_id = int(input("ID do Remédio: "))
            r = buscar_por_id(lista_farmacia, r_id)
            if r:
                lista_farmacia.remove(r)
                print("Remédio removido do catálogo.")
        
        elif opcao == '0':
            break