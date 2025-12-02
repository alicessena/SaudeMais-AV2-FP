from config import prontuarios_ref, pacientes_ref, profissionais_ref
import datetime


def _normalizar_pacientes():
    dados = pacientes_ref.get()
    if not dados:
        return []

    if isinstance(dados, dict):
        lista = []
        for key, value in dados.items():
            if isinstance(value, dict):
                if "cpf" not in value:
                    value["cpf"] = key
                lista.append(value)
        return lista

    if isinstance(dados, list):
        return [d for d in dados if isinstance(d, dict)]

    return []


def _normalizar_profissionais():
    dados = profissionais_ref.get()
    if not dados:
        return []

    lista = []
    for key, value in dados.items():
        if isinstance(value, dict):
            if "crm" not in value:
                value["crm"] = key
            lista.append(value)
    return lista


def _buscar(lista, campo, valor):
    for item in lista:
        if str(item.get(campo)).strip() == str(valor).strip():
            return item
    return None


def registrar_atendimento():
    pacientes = _normalizar_pacientes()
    profissionais = _normalizar_profissionais()

    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    if not profissionais:
        print("Nenhum profissional cadastrado.")
        return

    cpf = input("CPF do paciente: ").strip()
    paciente = _buscar(pacientes, "cpf", cpf)
    if not paciente:
        print("Paciente não encontrado.")
        return

    crm = input("CRM do profissional: ").strip()
    profissional = _buscar(profissionais, "crm", crm)
    if not profissional:
        print("Profissional não encontrado.")
        return

    queixa = input("Queixa principal: ").strip()
    diagnostico = input("Diagnóstico / Observações: ").strip()
    prescricao = input("Prescrição: ").strip()

    data_registro = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    novo_ref = prontuarios_ref.push()
    reg_id = novo_ref.key

    registro = {
        "id": reg_id,
        "paciente": {
            "nome": paciente["nome"],
            "cpf": paciente["cpf"]
        },
        "profissional": {
            "nome": profissional["nome"],
            "crm": profissional["crm"]
        },
        "data": data_registro,
        "queixa": queixa,
        "diagnostico": diagnostico,
        "prescricao": prescricao
    }

    novo_ref.set(registro)
    print(f"Atendimento registrado! ID: {reg_id}")


def consultar_historico():
    cpf = input("CPF do paciente: ").strip()
    historico = prontuarios_ref.get()

    if not historico:
        print("Nenhum prontuário cadastrado.")
        return

    print(f"\n=== HISTÓRICO DO PACIENTE {cpf} ===")
    encontrou = False

    for reg in historico.values():
        if reg.get("paciente", {}).get("cpf") == cpf:
            encontrou = True
            print(f"\n[ID: {reg['id']}] - Data: {reg['data']}")
            print(f"Médico: {reg['profissional']['nome']} (CRM: {reg['profissional']['crm']})")
            print(f"Queixa: {reg['queixa']}")
            print(f"Diagnóstico: {reg['diagnostico']}")
            print(f"Prescrição: {reg['prescricao']}")
            print("-" * 40)

    if not encontrou:
        print("Nenhum registro encontrado para este paciente.")


def editar_registro():
    reg_id = input("ID do registro a editar: ").strip()

    registro = prontuarios_ref.child(reg_id).get()
    if not registro:
        print("Registro não encontrado.")
        return

    print(f"Editando registro de {registro['paciente']['nome']} ({registro['data']})")

    novo_diag = input(f"Novo Diagnóstico ({registro['diagnostico']}): ").strip()
    nova_presc = input(f"Nova Prescrição ({registro['prescricao']}): ").strip()

    prontuarios_ref.child(reg_id).update({
        "diagnostico": novo_diag or registro["diagnostico"],
        "prescricao": nova_presc or registro["prescricao"]
    })

    print("Registro atualizado com sucesso.")


def remover_prontuario():
    reg_id = input("ID do prontuário que deseja remover: ").strip()

    registro = prontuarios_ref.child(reg_id).get()
    if not registro:
        print("Registro não encontrado.")
        return

    prontuarios_ref.child(reg_id).delete()
    print(f"Prontuário {reg_id} removido com sucesso.")