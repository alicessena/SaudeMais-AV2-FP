
def menu_relatorios(pacientes, profissionais, consultas, exames, farmacia):
    print("\n" + "="*30)
    print(" RELATÓRIOS DE GESTÃO UBS")
    print("="*30)
    
    print(f"Total de Pacientes: {len(pacientes)}")
    print(f"Total de Profissionais: {len(profissionais)}")
    print(f"Total de Consultas: {len(consultas)}")
    print(f"Total de Exames: {len(exames)}")
    print(f"Itens na Farmácia: {len(farmacia)}")
    
    print("\n--- Detalhamento de Consultas por Médico ---")
    contagem = {}
    for c in consultas:
        if c['status'] != 'Cancelada':
            medico = c['medico_nome']
            contagem[medico] = contagem.get(medico, 0) + 1
    
    if not contagem:
        print("Nenhuma consulta ativa registrada.")
    else:
        for med, qtd in contagem.items():
            print(f"- Dr(a). {med}: {qtd} consulta(s)")
    
    input("\nPressione Enter para voltar...")