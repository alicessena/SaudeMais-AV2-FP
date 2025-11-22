from utils import buscar_por_id, gerar_novo_id

def menu_consultas(lista_consultas, lista_pacientes, lista_profissionais):
    while True:
        print("\n--- GESTÃO DE CONSULTAS ---")
        print("1. Agendar Consulta")
        print("2. Visualizar Consultas")
        print("3. Reagendar/Editar Consulta")
        print("4. Cancelar Consulta")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            if not lista_pacientes or not lista_profissionais:
                print("Erro: É necessário ter pacientes e profissionais cadastrados.")
                continue
            
            try:
                p_id = int(input("ID do Paciente: "))
                m_id = int(input("ID do Profissional: "))
            except ValueError:
                print("Por favor, digite números válidos.")
                continue

            data = input("Data (dd/mm/aaaa): ")
            hora = input("Hora (hh:mm): ")
            
            paciente = buscar_por_id(lista_pacientes, p_id)
            medico = buscar_por_id(lista_profissionais, m_id)

            if paciente and medico:
                novo_id = gerar_novo_id(lista_consultas)
                consulta = {
                    'id': novo_id,
                    'paciente_nome': paciente['nome'],
                    'medico_nome': medico['nome'],
                    'data': data,
                    'hora': hora,
                    'status': 'Agendada'
                }
                lista_consultas.append(consulta)
                print(f"Consulta agendada com ID {novo_id}")
            else:
                print("Paciente ou Profissional não encontrado.")

        elif opcao == '2':
            for c in lista_consultas:
                print(f"ID: {c['id']} | Pcte: {c['paciente_nome']} | Méd: {c['medico_nome']} | Data: {c['data']} | Status: {c['status']}")

        elif opcao == '3':
            c_id = int(input("ID da Consulta: "))
            c = buscar_por_id(lista_consultas, c_id)
            if c:
                c['data'] = input(f"Nova Data ({c['data']}): ") or c['data']
                c['hora'] = input(f"Nova Hora ({c['hora']}): ") or c['hora']
                print("Reagendado!")

        elif opcao == '4':
            c_id = int(input("ID da Consulta: "))
            c = buscar_por_id(lista_consultas, c_id)
            if c:
                c['status'] = 'Cancelada'
                print("Consulta cancelada.")
        
        elif opcao == '0':
            break
    