from CRUD_Farmacia import (
    criar_medicamentos,
    listar_medicamentos,
    atualizar_medicamentos,
    remover_medicamentos
)

from CRUD_Pacientes import (
    cadastrar_paciente,
    listar_pacientes,
    atualizar_paciente,
    remover_paciente
)

from CRUD_Profissionais import (
    cadastrar_profissional,
    listar_profissionais,
    atualizar_profissional,
    remover_profissional
)

from CRUD_Consultas import (
    criar_consulta,
    listar_consultas,
    atualizar_consulta,
    remover_consulta
)

from CRUD_Exames import (
    solicitar_exame,
    listar_exames,
    registrar_resultado,
    cancelar_exame
)

from CRUD_Prontuarios import (
    registrar_atendimento,
    consultar_historico,
    editar_registro,
    remover_prontuario
)


from config import medicamentos_ref
from config import pacientes_ref
from config import profissionais_ref
from config import consultas_ref
from config import exames_ref
from config import prontuarios_ref


def main():
    while True:
        print("\n===== SISTEMA HOSPITALAR =====")
        print("1 - Gestão de Medicamentos")
        print("2 - Gestão de Pacientes")
        print("3 - Gestão de Profissionais")
        print("4 - Gestão de Consultas")
        print("5 - Gestão de Exames")
        print("6 - Gestão de Prontuários")
        print("0 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            menu_medicamentos()

        elif opc == "2":
            menu_pacientes()

        elif opc == "3":
            menu_profissionais()
        
        elif opc == "4":
            menu_consultas()
        
        elif opc == "5":
            menu_exames()

        elif opc == "6":
            menu_prontuarios()

        elif opc == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


def menu_medicamentos():
    while True:
        print("\n--- MENU MEDICAMENTOS ---")
        print("1 - Criar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Atualizar medicamento")
        print("4 - Remover medicamento")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            criar_medicamentos()
        elif op == "2":
            listar_medicamentos()
        elif op == "3":
            atualizar_medicamentos()
        elif op == "4":
            remover_medicamentos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu_pacientes():
    while True:
        print("\n--- MENU PACIENTES ---")
        print("1 - Cadastrar paciente")
        print("2 - Listar pacientes")
        print("3 - Atualizar paciente")
        print("4 - Remover paciente")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_paciente()
        elif op == "2":
            listar_pacientes()
        elif op == "3":
            atualizar_paciente()
        elif op == "4":
            remover_paciente()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_profissionais():
    while True:
        print("\n--- MENU PROFISSIONAIS ---")
        print("1 - Cadastrar Profissional")
        print("2 - Listar Profissionais")
        print("3 - Atualizar Profissional")
        print("4 - Remover Profissional")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            cadastrar_profissional()
        elif op == "2":
            listar_profissionais()
        elif op == "3":
            atualizar_profissional()
        elif op == "4":
            remover_profissional()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_consultas():
    while True:
        print("--- CONSULTAS ---")
        print("1 - Agendar Consulta")
        print("2 - Listar Consultas")
        print("3 - Reagendar Consulta")
        print("4 - Cancelar Consulta")
        print("0 - Voltar")
        op = input("Escolha: ")

        if op == "1":
            criar_consulta()
        elif op == "2":
            listar_consultas()
        elif op == "3":
            atualizar_consulta()
        elif op == "4":
            remover_consulta()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_exames():
    while True:
        print("-- EXAMES --")
        print("1 - Solicitar Exame")
        print("2 - Listar Exames")
        print("3 - Registrar Resultado")
        print("4 - Cancelar Exame")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            solicitar_exame()
        elif op == "2":
            listar_exames()
        elif op == "3":
            registrar_resultado()
        elif op == "4":
            cancelar_exame()
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_prontuarios():
    while True:
        print("--- PRONTUÁRIOS ---")
        print("1 - Registrar Atendimento")
        print("2 - Consultar Histórico")
        print("3 - Editar Registro")
        print("4 - Remover Registro")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            registrar_atendimento()
        elif op == "2":
            consultar_historico()
       	elif op == "3":
            editar_registro()
       	elif op == "4":
            remover_prontuario()
       	elif op == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__": 
    main()