import sys
from crud_pacientes import menu_pacientes
from crud_profissionais import menu_profissionais
from crud_consultas import menu_consultas
from crud_exames import menu_exames
from crud_farmacia import menu_farmacia
from relatorios import menu_relatorios

def main():
    db_pacientes = []
    db_profissionais = []
    db_consultas = []
    db_exames = []
    db_farmacia = []

    while True:
        print("\n" + "="*40)
        print(" SISTEMA INTEGRADO UBS - SAÚDE E BEM-ESTAR")
        print("="*40)
        print("1. Gestão de Pacientes")
        print("2. Gestão de Profissionais")
        print("3. Gestão de Consultas")
        print("4. Gestão de Exames")
        print("5. Farmácia")
        print("6. Relatórios Gerenciais")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_pacientes(db_pacientes)
        
        elif opcao == '2':
            menu_profissionais(db_profissionais)
        
        elif opcao == '3':
            menu_consultas(db_consultas, db_pacientes, db_profissionais)
        
        elif opcao == '4':
            menu_exames(db_exames, db_pacientes)
        
        elif opcao == '5':
            menu_farmacia(db_farmacia)
        
        elif opcao == '6':
            menu_relatorios(db_pacientes, db_profissionais, db_consultas, db_exames, db_farmacia)
        
        elif opcao == '0':
            print("Encerrando sistema...")
            sys.exit()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()