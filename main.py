import sys
import os
from utils import carregar_arquivo, salvar_arquivo
from crud_pacientes import menu_pacientes
from crud_profissionais import menu_profissionais
from crud_consultas import menu_consultas
from crud_exames import menu_exames
from crud_farmacia import menu_farmacia
from crud_prontuarios import menu_prontuarios  
from relatorios import menu_relatorios

PASTA_DADOS = "dados"

ARQ_PACIENTES = os.path.join(PASTA_DADOS, "pacientes.json")
ARQ_PROFISSIONAIS = os.path.join(PASTA_DADOS, "profissionais.json")
ARQ_CONSULTAS = os.path.join(PASTA_DADOS, "consultas.json")
ARQ_EXAMES = os.path.join(PASTA_DADOS, "exames.json")
ARQ_FARMACIA = os.path.join(PASTA_DADOS, "farmacia.json")
ARQ_PRONTUARIOS = os.path.join(PASTA_DADOS, "prontuarios.json") 

def inicializar_diretorio():
    if not os.path.exists(PASTA_DADOS):
        os.makedirs(PASTA_DADOS)

def main():
    inicializar_diretorio()

    print("Carregando banco de dados...")
    db_pacientes = carregar_arquivo(ARQ_PACIENTES)
    db_profissionais = carregar_arquivo(ARQ_PROFISSIONAIS)
    db_consultas = carregar_arquivo(ARQ_CONSULTAS)
    db_exames = carregar_arquivo(ARQ_EXAMES)
    db_farmacia = carregar_arquivo(ARQ_FARMACIA)
    db_prontuarios = carregar_arquivo(ARQ_PRONTUARIOS) 

    while True:
        print("\n" + "="*40)
        print(" SISTEMA INTEGRADO UBS COMPLETO")
        print("="*40)
        print("1. Gestão de Pacientes")
        print("2. Gestão de Profissionais")
        print("3. Gestão de Consultas")
        print("4. Gestão de Exames")
        print("5. Farmácia")
        print("6. Prontuários Médicos") 
        print("7. Relatórios Gerenciais")
        print("0. Sair e Salvar")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_pacientes(db_pacientes)
            salvar_arquivo(ARQ_PACIENTES, db_pacientes)
        
        elif opcao == '2':
            menu_profissionais(db_profissionais)
            salvar_arquivo(ARQ_PROFISSIONAIS, db_profissionais)
        
        elif opcao == '3':
            menu_consultas(db_consultas, db_pacientes, db_profissionais)
            salvar_arquivo(ARQ_CONSULTAS, db_consultas)
        
        elif opcao == '4':
            menu_exames(db_exames, db_pacientes)
            salvar_arquivo(ARQ_EXAMES, db_exames)
        
        elif opcao == '5':
            menu_farmacia(db_farmacia)
            salvar_arquivo(ARQ_FARMACIA, db_farmacia)
            
        elif opcao == '6':
            menu_prontuarios(db_prontuarios, db_pacientes, db_profissionais)
            salvar_arquivo(ARQ_PRONTUARIOS, db_prontuarios)

        elif opcao == '7':
            menu_relatorios(db_pacientes, db_profissionais, db_consultas, db_exames, db_farmacia)
        
        elif opcao == '0':
            print("Salvando todas as alterações...")
            salvar_arquivo(ARQ_PACIENTES, db_pacientes)
            salvar_arquivo(ARQ_PROFISSIONAIS, db_profissionais)
            salvar_arquivo(ARQ_CONSULTAS, db_consultas)
            salvar_arquivo(ARQ_EXAMES, db_exames)
            salvar_arquivo(ARQ_FARMACIA, db_farmacia)
            salvar_arquivo(ARQ_PRONTUARIOS, db_prontuarios) 
            print("Sistema encerrado.")
            sys.exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()