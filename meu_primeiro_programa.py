SALDO = 2000
CHEQUE_ESPECIAL = 1000
SAQUE: int
OPCAO = -1

def imprimir_separador():
    print("=" * 30)

def imprimir_mensagem(mensagem):
    imprimir_separador()
    print(mensagem)
    imprimir_separador()

def deseja_continuar():
    imprimir_separador()
    print("Deseja fazer outra operação?")
    print("3 - Sim")
    print("0 - Sair")
    imprimir_separador()
    return int(input("Digite a opção desejada: "))

while OPCAO != 0:
    imprimir_mensagem("Olá, seja bem-vindo ao Banco do Brasil")
    print("1 - Saldo")
    print("2 - Saque")
    print("0 - Sair")
    imprimir_separador()
    OPCAO = int(input("Digite a opção desejada: ")) 
    imprimir_separador()
    
    if OPCAO == 1:
        imprimir_mensagem(f"Seu saldo é de: {SALDO}\nSeu saldo especial é de: {CHEQUE_ESPECIAL}")
        OPCAO = deseja_continuar()
        if OPCAO == 0:
            imprimir_mensagem("Obrigado por utilizar o Banco do Brasil")
            break
    elif OPCAO == 2:
        SAQUE = int(input("Digite o valor do saque: "))
        if SAQUE <= SALDO:
            print("Saque realizado com sucesso")
            SALDO = SALDO - SAQUE
        elif SAQUE <= SALDO + CHEQUE_ESPECIAL:
            print("Saque realizado com sucesso usando cheque especial")
            CHEQUE_ESPECIAL = CHEQUE_ESPECIAL - (SAQUE - SALDO)
            SALDO = 0
        else:
            print("Saldo insuficiente")
        OPCAO = deseja_continuar()
        if OPCAO == 0:
            imprimir_mensagem("Obrigado por utilizar o Banco do Brasil")
            break
    elif OPCAO == 0:
        imprimir_mensagem("Obrigado por utilizar o Banco do Brasil")
        break  # Sai do loop e encerra o programa
    else:
        print("Opção inválida")

    # Exibir saldo e cheque especial após cada operação
    imprimir_mensagem(f"Seu saldo é de: {SALDO}\nCheque especial: {CHEQUE_ESPECIAL}")

# Mensagem final de encerramento
imprimir_separador()
