from utils import gerar_novo_id, buscar_por_crm, limpar_tela, ler_numero_valido

def menu_profissionais(lista_profissionais):
    while True:
        print("\n--- GESTÃO DE PROFISSIONAIS ---")
        print("1. Cadastrar Profissional")
        print("2. Listar Profissionais")
        print("3. Atualizar Profissional")
        print("4. Excluir Profissional")
        print("5. Consultar Profissional")
        print("0. Voltar") 
        opcao = ler_numero_valido("Escolha: ")
        
        if opcao == 1:
            nome = input("Nome do Profissional: ")
            especialidade = input("Especialidade: ")
            crm = ler_numero_valido("CRM/Registro: ")
            novo_id = gerar_novo_id(lista_profissionais)
            
            prof = {
                'id': novo_id, 
                'nome': nome, 
                'especialidade': especialidade, 
                'crm': crm}
            
            lista_profissionais.append(prof)
            print(f"Profissional cadastrado com ID {novo_id}.")
        
        elif opcao == 2:
            for p in lista_profissionais:
                print(f"ID: {p['id']} | Nome: {p['nome']} | Esp: {p['especialidade']}")

        elif opcao == 3:
            crm_p = ler_numero_valido("CRM do profissional: ")
            p = buscar_por_crm(lista_profissionais, crm_p)
            if p:
                p['nome'] = input(f"Novo nome ({p['nome']}): ") or p['nome'] #se a entrada for "" o python vai considerar falso entao p volta a ser p['nome'].
                p['especialidade'] = input(f"Nova especialidade ({p['especialidade']}): ") or p['especialidade'] #Mesma lógica que o de cima.
                print("Atualizado!")
        
        elif opcao == 4:
            crm_p = ler_numero_valido("CRM do profissional: ")
            p = buscar_por_crm(lista_profissionais, crm_p)
            if p:
                lista_profissionais.remove(p)
                print("Removido.")
        
        elif opcao == 5:
            crm_p = ler_numero_valido("CRM do profissional: ")
            p = buscar_por_crm(lista_profissionais, crm_p)
            if p:
                print(f"O profissional com o CRM: {crm_p} é {p['nome']}")
            else:
                print(f"O profissional com CRM: {crm_p}. Não foi encontrado.")
        
        elif opcao == 0:
            limpar_tela()
            break