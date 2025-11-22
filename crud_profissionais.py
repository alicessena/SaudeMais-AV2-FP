from utils import buscar_por_id, gerar_novo_id

def menu_profissionais(lista_profissionais):
    while True:
        print("\n--- GESTÃO DE PROFISSIONAIS ---")
        print("1. Cadastrar Profissional")
        print("2. Listar Profissionais")
        print("3. Atualizar Profissional")
        print("4. Excluir Profissional")
        print("0. Voltar")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome do Profissional: ")
            especialidade = input("Especialidade: ")
            crm = input("CRM/Registro: ")
            novo_id = gerar_novo_id(lista_profissionais)
            
            prof = {'id': novo_id, 'nome': nome, 'especialidade': especialidade, 'crm': crm}
            lista_profissionais.append(prof)
            print(f"Profissional cadastrado com ID {novo_id}.")
        
        elif opcao == '2':
            for p in lista_profissionais:
                print(f"ID: {p['id']} | Nome: {p['nome']} | Esp: {p['especialidade']}")

        elif opcao == '3':
            id_p = int(input("ID do profissional: "))
            p = buscar_por_id(lista_profissionais, id_p)
            if p:
                p['nome'] = input(f"Novo nome ({p['nome']}): ") or p['nome']
                p['especialidade'] = input(f"Nova especialidade ({p['especialidade']}): ") or p['especialidade']
                print("Atualizado!")
        
        elif opcao == '4':
            id_p = int(input("ID do profissional: "))
            p = buscar_por_id(lista_profissionais, id_p)
            if p:
                lista_profissionais.remove(p)
                print("Removido.")
        
        elif opcao == '0':
            break