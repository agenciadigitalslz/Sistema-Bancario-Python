# Constantes
SALDO_INICIAL = 2000
CHEQUE_ESPECIAL_INICIAL = 1000
OPCAO_SALDO = 1
OPCAO_SAQUE = 2
OPCAO_SAIR = 0
OPCAO_CONTINUAR = 3

# Variáveis globais
saldo = SALDO_INICIAL
cheque_especial = CHEQUE_ESPECIAL_INICIAL

def imprimir_separador():
    print("=" * 30)

def imprimir_mensagem(mensagem):
    imprimir_separador()
    print(mensagem)
    imprimir_separador()

def deseja_continuar():
    imprimir_separador()
    print("Deseja fazer outra operação?")
    print(f"{OPCAO_CONTINUAR} - Sim")
    print(f"{OPCAO_SAIR} - Sair")
    imprimir_separador()
    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        return OPCAO_SAIR

def consultar_saldo():
    imprimir_mensagem(f"Seu saldo é de: {saldo}\nSeu saldo especial é de: {cheque_especial}")

def realizar_saque():
    global saldo, cheque_especial
    try:
        valor_saque = int(input("Digite o valor do saque: "))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return

    if valor_saque <= saldo:
        saldo -= valor_saque
        print("Saque realizado com sucesso")
    elif valor_saque <= saldo + cheque_especial:
        cheque_especial -= (valor_saque - saldo)
        saldo = 0
        print("Saque realizado com sucesso usando cheque especial")
    else:
        print("Saldo insuficiente")

def exibir_menu():
    imprimir_mensagem("Olá, seja bem-vindo ao Banco do Brasil")
    print(f"{OPCAO_SALDO} - Saldo")
    print(f"{OPCAO_SAQUE} - Saque")
    print(f"{OPCAO_SAIR} - Sair")
    imprimir_separador()

def main():
    opcao = -1
    while opcao != OPCAO_SAIR:
        exibir_menu()
        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida. Tente novamente.")
            continue

        if opcao == OPCAO_SALDO:
            consultar_saldo()
            opcao = deseja_continuar()
        elif opcao == OPCAO_SAQUE:
            realizar_saque()
            opcao = deseja_continuar()
        elif opcao == OPCAO_SAIR:
            imprimir_mensagem("Obrigado por utilizar o Banco do Brasil")
            break
        else:
            print("Opção inválida")

        # Exibir saldo e cheque especial após cada operação, exceto ao sair
        if opcao != OPCAO_SAIR:
            consultar_saldo()

    # Mensagem final de encerramento
    imprimir_separador()

if __name__ == "__main__":
    main()