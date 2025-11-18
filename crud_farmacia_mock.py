import sys
from mock_medicamentos import mock_estoque

estoque = []
proximo_id = 1

def carregar_mock():
    global estoque, proximo_id
    
    estoque.extend(mock_estoque) 
    
    if estoque:
        proximo_id = estoque[-1]['id'] + 1
    
    print(f" {len(estoque)} medicamentos carregados do mock com sucesso!")

def solicitar_remedio():
    """CREATE: Adiciona um novo medicamento ao estoque."""
    global proximo_id
    print("\n--- Solicitar Remédio ---")
    
    nome = input("Nome do Remédio: ").strip()
    
    while True:
        try:
            quantidade = int(input("Quantidade Inicial: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    novo_med = {
        'id': proximo_id,
        'nome': nome,
        'quantidade': quantidade
    }
    
    estoque.append(novo_med) 
    proximo_id += 1
    
    print(f" Remédio '{nome}' (ID {novo_med['id']}) adicionado com sucesso.")

def consultar_estoque():
    """READ: Lista todos os medicamentos no estoque."""
    print("\n--- Estoque de Remédios ---")
    
    if not estoque:
        print("O estoque está vazio.")
        return

    print(f"{'ID':<4} | {'Nome':<25} | {'Quantidade':<10}")
    print("-" * 43)

    for med in estoque:
        print(f"{med['id']:<4} | {med['nome']:<25} | {med['quantidade']:<10}")

def registrar_retirada():
    """UPDATE: Diminui a quantidade (registra retirada) de um remédio."""
    print("\n--- Registrar Retirada ---")
    
    try:
        id_busca = int(input("ID do Remédio para retirada: "))
    except ValueError:
        print(" ID inválido. Digite um número inteiro.")
        return

    for med in estoque:
        if med['id'] == id_busca:
            print(f"Remédio encontrado: {med['nome']}. Quantidade atual: {med['quantidade']}")
            
            while True:
                try:
                    retirada = int(input("Quantidade a ser retirada: "))
                    if retirada <= 0:
                        print("A retirada deve ser maior que zero.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
            
            if retirada <= med['quantidade']:
                med['quantidade'] -= retirada # Atualiza a quantidade
                print(f" Retirada de {retirada} unidades de '{med['nome']}' registrada. Novo estoque: {med['quantidade']}")
            else:
                print(f" Erro: Retirada de {retirada} é maior que o estoque atual de {med['quantidade']}.")
            return
            
    print(f" Remédio com ID {id_busca} não encontrado.")

def remedio_em_falta():
    """DELETE: Remove um medicamento do estoque."""
    print("\n--- Remédio em Falta (Excluir) ---")
    
    try:
        id_busca = int(input("ID do Remédio que será removido: "))
    except ValueError:
        print(" ID inválido. Digite um número inteiro.")
        return

    for i, med in enumerate(estoque):
        if med['id'] == id_busca:
            nome_removido = med['nome']
            del estoque[i] 
            print(f" Remédio '{nome_removido}' (ID {id_busca}) removido do estoque.")
            return

    print(f" Remédio com ID {id_busca} não encontrado.")


def menu():
    """Exibe o menu de opções."""
    opcoes = {
        '1': solicitar_remedio,
        '2': consultar_estoque,
        '3': registrar_retirada,
        '4': remedio_em_falta
    }
    
    carregar_mock() 

    while True:
        print("\n--- Gestão de Farmácia (Python) ---")
        print("1 - Solicitar Remédio")
        print("2 - Consultar Estoque)")
        print("3 - Registrar Retirada")
        print("4 - Remédio em Falta")
        print("0 - Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '0':
            print("Saindo do sistema. Até a próxima!")
            sys.exit()
        
        if escolha in opcoes:
            opcoes[escolha]()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()