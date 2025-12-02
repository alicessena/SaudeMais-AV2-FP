from config import consultas_ref, pacientes_ref, profissionais_ref

def _listar_pacientes():
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



def _listar_profissionais():
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
        if str(item.get(campo)) == str(valor):
            return item
    return None



def criar_consulta():
    pacientes = _listar_pacientes()
    profissionais = _listar_profissionais()

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
        print("\nProfissionais cadastrados:")
        for p in profissionais:
            print(f"Nome: {p['nome']} | CRM: {p['crm']}")
        return

    data = input("Data (dd/mm/aaaa): ").strip()
    hora = input("Hora (hh:mm): ").strip()

    ref = consultas_ref.push()
    cid = ref.key

    consulta = {
        "id": cid,
        "paciente": {
            "nome": paciente["nome"],
            "cpf": paciente["cpf"]
        },
        "profissional": {
            "nome": profissional["nome"],
            "crm": profissional["crm"]
        },
        "data": data,
        "hora": hora,
        "status": "Agendada"
    }

    ref.set(consulta)
    print(f"Consulta agendada com sucesso! ID: {cid}")


def listar_consultas():
    dados = consultas_ref.get()

    if not dados:
        print("Nenhuma consulta cadastrada.")
        return

    print("\n--- LISTA DE CONSULTAS ---")
    for c in dados.values():
        print(
            f"ID: {c['id']} | "
            f"Paciente: {c['paciente']['nome']} | "
            f"Profissional: {c['profissional']['nome']} (CRM: {c['profissional']['crm']}) | "
            f"{c['data']} {c['hora']} | Status: {c['status']}"
        )



def atualizar_consulta():
    cid = input("ID da consulta: ").strip()
    consulta = consultas_ref.child(cid).get()

    if not consulta:
        print("Consulta não encontrada.")
        return

    nova_data = input(f"Nova data ({consulta['data']}): ").strip() or consulta["data"]
    nova_hora = input(f"Nova hora ({consulta['hora']}): ").strip() or consulta["hora"]

    consultas_ref.child(cid).update({
        "data": nova_data,
        "hora": nova_hora
    })

    print("Consulta reagendada com sucesso.")



def remover_consulta():
    cid = input("ID da consulta: ").strip()
    consulta = consultas_ref.child(cid).get()

    if not consulta:
        print("Consulta não encontrada.")
        return

    consultas_ref.child(cid).update({"status": "Cancelada"})
    print("Consulta cancelada com sucesso.")