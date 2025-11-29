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
                print("ID inválido. Por favor, digite apenas números.")
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
                print(f"Exame de {tipo} para {paciente['nome']} solicitado com ID: {novo_id}.")
            else:
                print("Paciente não encontrado.")
        
        elif opcao == '2':
            print("\n--- LISTA DE EXAMES ---")
            if not lista_exames:
                print("Nenhum exame registrado.")
            for e in lista_exames:
                # Melhorando a exibição para incluir o status
                print(f"ID: {e['id']} | Paciente: {e['paciente']} | Tipo: {e['tipo']} | Resultado: {e['resultado']} | Status: {e['status']}")

        elif opcao == '3':
            try:
                e_id = int(input("ID do Exame para registrar resultado: "))
            except ValueError:
                print("ID inválido. Por favor, digite apenas números.")
                continue
            
            e = buscar_por_id(lista_exames, e_id)
            if e:
                if e['status'] == 'Concluido':
                     print("Aviso: Este exame já está concluído. Você está sobrescrevendo o resultado.")
                e['resultado'] = input(f"Novo Resultado para ID {e_id} ({e['tipo']}): ")
                e['status'] = 'Concluido'
                print("Resultado salvo e status atualizado para 'Concluido'.")
            else:
                print("Exame não encontrado.")

        elif opcao == '4':
            try:
                e_id = int(input("ID do Exame para cancelar: "))
            except ValueError:
                print("ID inválido. Por favor, digite apenas números.")
                continue

            e = buscar_por_id(lista_exames, e_id)
            if e:
                lista_exames.remove(e)
                print(f"Exame {e_id} ({e['tipo']}) cancelado e removido.")
            else:
                print("Exame não encontrado.")

        elif opcao == '0':
            break
        
        else:
            print("Opção inválida. Escolha um número entre 0 e 4.")
