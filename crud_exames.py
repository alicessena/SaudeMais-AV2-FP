from utils import buscar_por_id, gerar_novo_id

def menu_exames(lista_exames, lista_pacientes):
    while True:
        print("\n--- GESTÃO DE EXAMES ---")
        print("1. Solicitar Exame")
        print("2. Consultar Exames")
        print("3. Registrar Resultado")
        print("4. Cancelar Exame")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            try:
                p_id = int(input("ID do Paciente: "))
            except ValueError:
                print("ID inválido.")
                continue

            tipo = input("Tipo de Exame (ex: Hemograma): ")
            paciente = buscar_por_id(lista_pacientes, p_id)
            
            if paciente:
                novo_id = gerar_novo_id(lista_exames)
                exame = {
                    'id': novo_id,
                    'paciente': paciente['nome'],
                    'tipo': tipo,
                    'resultado': 'Pendente',
                    'status': 'Solicitado'
                }
                lista_exames.append(exame)
                print("Exame solicitado.")
            else:
                print("Paciente não encontrado.")
        
        elif opcao == '2':
            for e in lista_exames:
                print(f"ID: {e['id']} | Paciente: {e['paciente']} | Tipo: {e['tipo']} | Res: {e['resultado']}")

        elif opcao == '3':
            e_id = int(input("ID do Exame: "))
            e = buscar_por_id(lista_exames, e_id)
            if e:
                e['resultado'] = input("Resultado do exame: ")
                e['status'] = 'Concluido'
                print("Resultado salvo.")

        elif opcao == '4':
            e_id = int(input("ID do Exame: "))
            e = buscar_por_id(lista_exames, e_id)
            if e:
                lista_exames.remove(e)
                print("Exame cancelado.")

        elif opcao == '0':
            break