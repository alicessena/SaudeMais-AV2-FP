from utils import buscar_por_id, gerar_novo_id

def menu_pacientes(lista_pacientes):
    while True:
        print("\n--- GESTÃO DE PACIENTES ---")
        print("1. Cadastrar Paciente")
        print("2. Listar Pacientes")
        print("3. Atualizar Paciente")
        print("4. Excluir Paciente")
        print("5. Buscar Paciente")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome do Paciente: ")
            cpf = input("CPF: ")
            nasc = input("Data Nascimento (dd/mm/aaaa): ")
            novo_id = gerar_novo_id(lista_pacientes)
            
            paciente = {'id': novo_id, 'nome': nome, 'cpf': cpf, 'nasc': nasc}
            lista_pacientes.append(paciente)
            print(f"Paciente cadastrado com ID {novo_id}.")
        
        elif opcao == '2':
            print("\nLista de Pacientes:")
            for p in lista_pacientes:
                print(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']}")
        
        elif opcao == '3':
            id_p = int(input("ID do paciente para atualizar: "))
            p = buscar_por_id(lista_pacientes, id_p)
            if p:
                p['nome'] = input(f"Novo nome ({p['nome']}): ") or p['nome']
                p['cpf'] = input(f"Novo CPF ({p['cpf']}): ") or p['cpf']
                print("Dados atualizados!")
            else:
                print("Paciente não encontrado.")

        elif opcao == '4':
            id_p = int(input("ID do paciente para excluir: "))
            p = buscar_por_id(lista_pacientes, id_p)
            if p:
                lista_pacientes.remove(p)
                print("Paciente removido.")
            else:
                print("Paciente não encontrado.")
        
        elif opcao == '5':
            id_p = int (input("ID do paciente para buscar: "))
            p = buscar_por_id(lista_pacientes, id_p)
            if p:
                print(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Nascimento: {p['nasc']}")
            else:
                print("Paciente não encontrado.")

        elif opcao == '0':
            break