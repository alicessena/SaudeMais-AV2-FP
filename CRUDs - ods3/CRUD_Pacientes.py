from config import pacientes_ref


def cadastrar_paciente():
    print("\n--- Cadastro de Paciente ---")

    nome = input("Nome: ").strip()
    if nome == "":
        print("Nome inválido.")
        return

    cpf = input("CPF (apenas números): ").strip()
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido.")
        return

    nasc = input("Data de nascimento (dd/mm/aaaa): ").strip()
    if nasc == "":
        print("Data inválida.")
        return

    paciente_ref = pacientes_ref.child(cpf)

    existente = paciente_ref.get()
    if existente:
        print("\n--- Paciente encontrado no sistema ---")
        print(f"Nome: {existente.get('nome')}")
        print(f"CPF: {existente.get('cpf')}")
        print(f"Nascimento: {existente.get('nasc')}")
        print("--------------------------------")
        return


    paciente_ref.set({
        "nome": nome,
        "cpf": cpf,
        "nasc": nasc
    })

    print("Paciente cadastrado com sucesso!")


def listar_pacientes():
    print("\n--- Lista de Pacientes ---")

    dados = pacientes_ref.get()

    if not dados:
        print("Nenhum paciente cadastrado.")
        return

    if isinstance(dados, list):
        lista = [p for p in dados if isinstance(p, dict)]
    else:
        lista = list(dados.values())

    lista = sorted(lista, key=lambda x: x.get("nome", ""))

    for p in lista:
        print(f"Nome: {p['nome']} | CPF: {p['cpf']} | Nasc: {p['nasc']}")


def atualizar_paciente():
    print("\n--- Atualizar Paciente ---")

    cpf = input("Digite o CPF do paciente: ").strip()

    paciente_ref = pacientes_ref.child(cpf)
    dados = paciente_ref.get()

    if dados is None:
        print("Paciente não encontrado.")
        return

    novo_nome = input(f"Novo nome ({dados['nome']}): ").strip()
    nova_nasc = input(f"Nova data de nascimento ({dados['nasc']}): ").strip()

    if novo_nome:
        dados['nome'] = novo_nome

    if nova_nasc:
        dados['nasc'] = nova_nasc

    paciente_ref.update(dados)
    print("Dados atualizados com sucesso!")


def remover_paciente():
    print("\n--- Remover Paciente ---")

    cpf = input("CPF do paciente: ").strip()
    paciente_ref = pacientes_ref.child(cpf)

    if paciente_ref.get() is None:
        print("Paciente não encontrado.")
        return

    paciente_ref.delete()
    print("Paciente removido com sucesso!")