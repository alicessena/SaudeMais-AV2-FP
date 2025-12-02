from config import exames_ref, pacientes_ref

def _normalizar_pacientes():
    dados = pacientes_ref.get()
    if not dados:
        return []

    if isinstance(dados, list):
        return [p for p in dados if isinstance(p, dict)]

    if isinstance(dados, dict):
        lista = []
        for key, value in dados.items():
            if isinstance(value, dict):
                if "cpf" not in value:
                    value["cpf"] = key
                lista.append(value)
        return lista

    return []


def _buscar(lista, campo, valor):
    for item in lista:
        if str(item.get(campo)).strip() == str(valor).strip():
            return item
    return None


def solicitar_exame():
    pacientes = _normalizar_pacientes()

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    cpf = input("CPF do paciente: ").strip()
    paciente = _buscar(pacientes, "cpf", cpf)

    if not paciente:
        print("Paciente não encontrado.")
        return

    tipo = input("Tipo de exame (ex: Hemograma): ").strip()

    novo_ref = exames_ref.push()
    exame_id = novo_ref.key

    exame = {
        "id": exame_id,
        "paciente": {
            "nome": paciente["nome"],
            "cpf": paciente["cpf"]
        },
        "tipo": tipo,
        "resultado": "Pendente",
        "status": "Solicitado"
    }

    novo_ref.set(exame)
    print(f"Exame solicitado! ID: {exame_id}")


def listar_exames():
    dados = exames_ref.get()

    if not dados:
        print("Nenhum exame cadastrado.")
        return

    if isinstance(dados, dict):
        lista = list(dados.values())
    elif isinstance(dados, list):
        lista = [d for d in dados if isinstance(d, dict)]
    else:
        lista = []

    print("\n--- LISTA DE EXAMES ---")
    for e in lista:
        print(
            f"ID: {e.get('id')} | "
            f"Paciente: {e.get('paciente', {}).get('nome')} | "
            f"Tipo: {e.get('tipo')} | "
            f"Resultado: {e.get('resultado')} | "
            f"Status: {e.get('status')}"
        )


def registrar_resultado():
    e_id = input("ID do exame: ").strip()
    exame = exames_ref.child(e_id).get()

    if not exame:
        print("Exame não encontrado.")
        return

    resultado = input(f"Novo resultado ({exame['tipo']}): ").strip()

    exames_ref.child(e_id).update({
        "resultado": resultado,
        "status": "Concluido"
    })

    print("Resultado registrado com sucesso!")


def cancelar_exame():
    e_id = input("ID do exame a cancelar: ").strip()
    exame = exames_ref.child(e_id).get()

    if not exame:
        print("Exame não encontrado.")
        return

    exames_ref.child(e_id).delete()
    print(f"Exame {e_id} cancelado e removido.")
