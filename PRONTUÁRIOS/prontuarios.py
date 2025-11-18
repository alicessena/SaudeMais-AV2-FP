from arquivos import carregar_dados, salvar_dados

def criar_prontuario(prontuarios):
    print("\n" + "=" * 80)
    print("➕ CRIAR NOVO PRONTUÁRIO")
    print("=" * 80)
    
    queixa = input('Qual a principal queixa do paciente? ')
    historico_doenca = input('Descreva o histórico de doenças do paciente: ')
    cirugias_hospitais = input('O paciente já passou por cirurgias ou internações? ')
    habitos = input('Possui algum hábito prejudicial à saúde? ')
    historico_familiar = input('Tem histórico familiar de doenças? ')
    alergias = input('O paciente possui alguma alergia? ')
    medicacao = input('O paciente está fazendo uso de alguma medicação? ')
    diagnostico = input('Qual o diagnóstico do paciente? ')
    exames = input('Quais os exames devem ser solicitados? ')
    medicacao2 = input('Qual a medicação prescrita? ')
    retorno = input('O paciente deve retornar para uma nova consulta? Se sim, qual a data? ')

    prontuario = {
        'id': len(prontuarios) + 1,
        'queixa': queixa,
        'historico_doenca': historico_doenca,
        'cirugias_hospitais': cirugias_hospitais,
        'habitos': habitos,
        'historico_familiar': historico_familiar,
        'alergias': alergias,
        'medicacao': medicacao,
        'diagnostico': diagnostico,
        'exames': exames,
        'medicacao2': medicacao2,
        'retorno': retorno
    }

    prontuarios.append(prontuario)
    salvar_dados(prontuarios)
    print('✅ Prontuário criado com sucesso!\n')

def ler_todos(prontuarios):
    if not prontuarios:
        print('❌ Nenhum prontuário encontrado!')
        return
    
    print('\n📋 LISTA DE PRONTUÁRIOS:')
    print("=" * 80)
    for f in prontuarios:
        print(f"ID: {f['id']} | Queixa: {f['queixa']} | Diagnóstico: {f['diagnostico']}")
    print("=" * 80 + "\n")

def ler_um(prontuarios):
    if not prontuarios:
        print('❌ Nenhum prontuário encontrado!')
        return
    
    try:
        id_prontuario = int(input('Digite o ID do prontuário que deseja ler: '))
        for f in prontuarios:
            if f['id'] == id_prontuario:
                print('\n📄 PRONTUÁRIO ENCONTRADO:')
                print("=" * 80)
                print(f"ID: {f['id']}")
                print(f"Queixa: {f['queixa']}")
                print(f"Histórico de Doenças: {f['historico_doenca']}")
                print(f"Cirurgias/Internações: {f['cirugias_hospitais']}")
                print(f"Hábitos: {f['habitos']}")
                print(f"Histórico Familiar: {f['historico_familiar']}")
                print(f"Alergias: {f['alergias']}")
                print(f"Medicação em Uso: {f['medicacao']}")
                print(f"Diagnóstico: {f['diagnostico']}")
                print(f"Exames Solicitados: {f['exames']}")
                print(f"Medicação Prescrita: {f['medicacao2']}")
                print(f"Retorno: {f['retorno']}")
                print("=" * 80 + "\n")
                return
        print('❌ Prontuário não encontrado!')
    except ValueError:
        print('❌ ID inválido!')

def atualizar_prontuario(prontuarios):
    ler_todos(prontuarios)
    try:
        id_prontuario = int(input('Digite o ID do prontuário que deseja atualizar: '))
        for f in prontuarios:
            if f['id'] == id_prontuario:
                print('✏️ Prontuário encontrado. Deixe em branco para manter o valor atual.\n')
                
                queixa = input(f'Atualizar queixa ({f["queixa"]}): ') or f['queixa']
                historico_doenca = input(f'Atualizar histórico de doenças ({f["historico_doenca"]}): ') or f['historico_doenca']
                cirugias_hospitais = input(f'Atualizar cirurgias ou internações ({f["cirugias_hospitais"]}): ') or f['cirugias_hospitais']
                habitos = input(f'Atualizar hábitos prejudiciais à saúde ({f["habitos"]}): ') or f['habitos']
                historico_familiar = input(f'Atualizar histórico familiar de doenças ({f["historico_familiar"]}): ') or f['historico_familiar']
                alergias = input(f'Atualizar alergias ({f["alergias"]}): ') or f['alergias']
                medicacao = input(f'Atualizar medicação em uso ({f["medicacao"]}): ') or f['medicacao']
                diagnostico = input(f'Atualizar diagnóstico ({f["diagnostico"]}): ') or f['diagnostico']
                exames = input(f'Atualizar exames solicitados ({f["exames"]}): ') or f['exames']
                medicacao2 = input(f'Atualizar medicação prescrita ({f["medicacao2"]}): ') or f['medicacao2']
                retorno = input(f'Atualizar data de retorno ({f["retorno"]}): ') or f['retorno']

                f.update({
                    'queixa': queixa,
                    'historico_doenca': historico_doenca,
                    'cirugias_hospitais': cirugias_hospitais,
                    'habitos': habitos,
                    'historico_familiar': historico_familiar,
                    'alergias': alergias,
                    'medicacao': medicacao,
                    'diagnostico': diagnostico,
                    'exames': exames,
                    'medicacao2': medicacao2,
                    'retorno': retorno
                })

                salvar_dados(prontuarios)
                print('✅ Prontuário atualizado com sucesso!\n')
                return
        print('❌ Prontuário não encontrado!')
    except ValueError:
        print('❌ ID inválido!')


def deletar_prontuario(prontuarios):
    """Deleta um prontuário pelo ID"""
    ler_todos(prontuarios)
    
    if not prontuarios:
        print('❌ Nenhum prontuário encontrado!')
        return
    
    try:
        id_prontuario = int(input('Digite o ID do prontuário que deseja deletar: '))
        for f in prontuarios:
            if f['id'] == id_prontuario:
                confirmacao = input(f"⚠️ Tem certeza que deseja deletar o prontuário ID {id_prontuario}? (S/N): ").upper()
                if confirmacao == 'S':
                    prontuarios.remove(f)
                    salvar_dados(prontuarios)
                    print('✅ Prontuário deletado com sucesso!\n')
                else:
                    print('❌ Operação cancelada.\n')
                return
        print('❌ Prontuário não encontrado!')
    except ValueError:
        print('❌ ID inválido!')

def deletar_prontuario(prontuarios):
    ler_todos(prontuarios)
    try:
        id_prontuario = int(input('Digite o ID do prontuário que deseja apagar: '))
        for f in prontuarios:
            if f['id'] == id_prontuario:
                prontuarios.remove(f)
                salvar_dados(prontuarios)
                print('Prontuário apagado com sucesso!')
                return
        print('Prontuário não encontrado!')
    except ValueError:
        print('ID inválido!')