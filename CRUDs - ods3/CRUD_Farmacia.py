from config import medicamentos_ref

def criar_medicamentos():
    print("--- Criando Medicamento ---")
    
    while True:
        nome_med = input("Digite o nome do medicamento: ").strip().lower()
        if nome_med != "":
            break
        print("Por favor, insira um nome válido.")

    medi_ref = medicamentos_ref.child(nome_med)

    existente = medi_ref.get()
    if existente:
        print("\n--- Medicamento já cadastrado ---")
        print(f"Nome: {existente.get('nome')}")
        print(f"Tarja: {existente.get('tarja')}")
        print("----------------------------------")
        return


    while True:
        print("Digite a tarja do medicamento (B, A, V, P):")
        print("B - Tarja Branca")
        print("A - Tarja Amarela")
        print("V - Tarja Vermelha")
        print("P - Tarja Preta")
        
        tarja = input().lower()
        if tarja in ('b', 'a', 'v', 'p'):
            break
        print("Tarja inválida. Tente novamente.")

    medi_dict = {
        'nome': nome_med,
        'tarja': tarja
    }
    medi_ref.set(medi_dict)
    print("Medicamento criado com sucesso.")


def listar_medicamentos():
    todas = medicamentos_ref.get()
    
    if not todas:
        print("Não há medicamentos cadastrados.")
        return

    if isinstance(todas, list):
        lista = [m for m in todas if isinstance(m, dict)]
    else:
        lista = [m for m in todas.values() if isinstance(m, dict)]

    medicamentos_ordenados = sorted(
        lista,
        key=lambda m: m.get('nome', "")
    )

    print("\n-- Medicamentos --")
    for m in medicamentos_ordenados:
        nome = m.get('nome')
        tarja_code = m.get('tarja')
        
        tarja = {
            'b': 'Branca',
            'a': 'Amarela',
            'v': 'Vermelha',
            'p': 'Preta'
        }.get(tarja_code, 'Indefinida')
        
        print(f"Medicamento: {nome} | Tarja: {tarja}")


def atualizar_medicamentos():
    print("--- Atualizando Medicamento ---")
    
    nome_med = input("Digite o nome do medicamento que deseja atualizar: ").strip().lower()

    medi_ref = medicamentos_ref.child(nome_med)

    if medi_ref.get() is None:
        print("Medicamento não encontrado.")
        return

    while True:
        print("Digite o novo status do medicamento (B, A, V, P):")
        print("B - Tarja Branca")
        print("A - Tarja Amarela")
        print("V - Tarja Vermelha")
        print("P - Tarja Preta")
        
        tarja_medi = input().lower()

        if tarja_medi in ('b', 'a', 'v', 'p'):
            break
        print("Status inválido. Tente novamente.")

    medi_ref.update({'status': tarja_medi})
    print("Medicamento atualizado com sucesso.")


def remover_medicamentos():
    print("--- Removendo Medicamento ---")

    nome_med = input("Digite o nome do medicamento que você deseja remover: ").strip().lower()

    medi_ref = medicamentos_ref.child(nome_med)

    if medi_ref.get() is None:
        print("Medicamento não encontrado.")
        return

    medi_ref.delete()
    print("Medicamento removido com sucesso.")