from config import profissionais_ref

def cadastrar_profissional():
    print("\n--- Cadastro de Profissional ---")

    nome = input("Nome do profissional: ").strip()
    if nome == "":
        print("Nome inválido.")
        return

    especialidade = input("Especialidade: ").strip()
    if especialidade == "":
        print("Especialidade inválida.")
        return

    crm = input("CRM/Registro (somente números): ").strip()
    if not crm.isdigit():
        print("CRM inválido, digite apenas números.")
        return

    prof_ref = profissionais_ref.child(crm)

    existente = profissionais_ref.child(crm).get()

    if existente:
        print("\n--- Profissional encontrado no sistema ---")
        print(f"Nome: {existente.get('nome')}")
        print(f"Especialidade: {existente.get('especialidade')}")
        print(f"CRM: {existente.get('crm')}")
        print("----------------------------------")
        return


    prof_ref.set({
        "nome": nome,
        "especialidade": especialidade,
        "crm": crm
    })

    print("Profissional cadastrado com sucesso!")


def listar_profissionais():
    print("\n--- Lista de Profissionais ---")

    dados = profissionais_ref.get()

    if not dados:
        print("Nenhum profissional cadastrado.")
        return

    if isinstance(dados, list):
        lista = [p for p in dados if isinstance(p, dict)]
    else:
        lista = list(dados.values())

    lista = sorted(lista, key=lambda p: p.get("nome", ""))

    for p in lista:
        print(f"Nome: {p['nome']} | CRM: {p['crm']} | Especialidade: {p['especialidade']}")


def atualizar_profissional():
    print("\n--- Atualizar Profissional ---")

    crm = input("Digite o CRM do profissional: ").strip()
    prof_ref = profissionais_ref.child(crm)
    dados = prof_ref.get()

    if dados is None:
        print("Profissional não encontrado.")
        return

    novo_nome = input(f"Novo nome ({dados['nome']}): ").strip()
    nova_esp = input(f"Nova especialidade ({dados['especialidade']}): ").strip()

    if novo_nome:
        dados["nome"] = novo_nome
    if nova_esp:
        dados["especialidade"] = nova_esp

    prof_ref.update(dados)
    print("Profissional atualizado com sucesso!")


def remover_profissional():
    print("\n--- Remover Profissional ---")

    crm = input("CRM do profissional: ").strip()
    prof_ref = profissionais_ref.child(crm)

    if prof_ref.get() is None:
        print("Profissional não encontrado.")
        return

    prof_ref.delete()
    print("Profissional removido com sucesso!")