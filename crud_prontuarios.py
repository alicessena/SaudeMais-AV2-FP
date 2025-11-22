from utils import buscar_por_id, gerar_novo_id
import datetime

def menu_prontuarios(lista_prontuarios, lista_pacientes, lista_profissionais):
    while True:
        print("\n--- GESTÃO DE PRONTUÁRIOS (HISTÓRICO) ---")
        print("1. Registrar Novo Atendimento (Evolução)")
        print("2. Consultar Histórico de um Paciente")
        print("3. Editar Registro de Prontuário")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            try:
                p_id = int(input("ID do Paciente: "))
                m_id = int(input("ID do Profissional (Médico): "))
            except ValueError:
                print("IDs devem ser números.")
                continue

            paciente = buscar_por_id(lista_pacientes, p_id)
            medico = buscar_por_id(lista_profissionais, m_id)

            if paciente and medico:
                queixa = input("Queixa Principal/Motivo: ")
                diagnostico = input("Diagnóstico/Observações: ")
                prescricao = input("Prescrição (Remédios/Procedimentos): ")
                
                data_registro = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

                novo_id = gerar_novo_id(lista_prontuarios)
                registro = {
                    'id': novo_id,
                    'paciente_id': p_id,
                    'paciente_nome': paciente['nome'],
                    'medico_nome': medico['nome'],
                    'data': data_registro,
                    'queixa': queixa,
                    'diagnostico': diagnostico,
                    'prescricao': prescricao
                }
                lista_prontuarios.append(registro)
                print(f"Prontuário registrado com sucesso! ID: {novo_id}")
            else:
                print("Paciente ou Médico não encontrado.")

        elif opcao == '2':
            try:
                p_id = int(input("Digite o ID do Paciente para ver o histórico: "))
            except ValueError:
                continue

            paciente = buscar_por_id(lista_pacientes, p_id)
            if not paciente:
                print("Paciente não encontrado.")
                continue

            print(f"\n=== HISTÓRICO DE: {paciente['nome']} ===")
            encontrou = False
            for reg in lista_prontuarios:
                if reg['paciente_id'] == p_id:
                    print(f"\n[ID: {reg['id']}] - Data: {reg['data']}")
                    print(f"Médico: {reg['medico_nome']}")
                    print(f"Queixa: {reg['queixa']}")
                    print(f"Diagnóstico: {reg['diagnostico']}")
                    print(f"Prescrição: {reg['prescricao']}")
                    print("-" * 30)
                    encontrou = True
            
            if not encontrou:
                print("Nenhum registro encontrado para este paciente.")

        elif opcao == '3':
            pront_id = int(input("ID do Registro de Prontuário para editar: "))
            reg = buscar_por_id(lista_prontuarios, pront_id)
            if reg:
                print(f"Editando registro de {reg['paciente_nome']} feito em {reg['data']}")
                reg['diagnostico'] = input(f"Novo Diagnóstico ({reg['diagnostico']}): ") or reg['diagnostico']
                reg['prescricao'] = input(f"Nova Prescrição ({reg['prescricao']}): ") or reg['prescricao']
                print("Registro atualizado.")
            else:
                print("Registro não encontrado.")

        elif opcao == '0':
            break