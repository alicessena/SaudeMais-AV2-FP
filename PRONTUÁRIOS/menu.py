from arquivos import carregar_dados, salvar_dados
from prontuarios import criar_prontuario, ler_todos, ler_um, atualizar_prontuario, deletar_prontuario


def exibir_menu():
    while True:
        prontuarios = carregar_dados()  # Recarrega dados a cada iteração
        
        print("\n" + "=" * 50)
        print("🏥 SISTEMA DE PRONTUÁRIOS")
        print("=" * 50)
        print("1 - Cadastrar novo prontuário")
        print("2 - Ler todos os prontuários")
        print("3 - Ler um prontuário específico")
        print("4 - Atualizar prontuário")
        print("5 - Excluir prontuário")
        print("6 - Sair")
        print("=" * 50)
        
        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == "1":
            criar_prontuario(prontuarios)
        elif opcao == "2":
            ler_todos(prontuarios)
        elif opcao == "3":
            ler_um(prontuarios)
        elif opcao == "4":
            atualizar_prontuario(prontuarios)
        elif opcao == "5":
            deletar_prontuario(prontuarios)
        elif opcao == "6":
            print("👋 Saindo... até a próxima!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    exibir_menu()
