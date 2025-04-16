# Constantes
SALDO_INICIAL = 2000
CHEQUE_ESPECIAL_INICIAL = 1000

class Transacao:
    def registrar(self, conta):
        pass  # Método a ser implementado nas subclasses

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def exibir_historico(self):
        for transacao in self.transacoes:
            print(f"{transacao.__class__.__name__}: R$ {transacao.valor}")

class Conta:
    def __init__(self, cliente, numero):
        self.saldo = SALDO_INICIAL
        self.numero = numero
        self.cliente = cliente
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.adicionar_transacao(Deposito(valor))

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        else:
            return False

    def consultar_saldo(self):
        return self.saldo

    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print(f"Transferência de R$ {valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente para transferência.")

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar(self, cpf):
        return self.cpf == cpf

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite, limite_saques):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

def imprimir_menu():
    print("Olá, seja bem-vindo ao Banco do Brasil")
    print("==============================")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Transferência")
    print("4 - Histórico de Transações")
    print("5 - Sair")
    print("==============================")

def main():
    # Exemplo de uso
    cliente1 = Cliente("123.456.789-00", "João Silva", "Rua A, 123")
    conta1 = ContaCorrente(cliente1, 1, CHEQUE_ESPECIAL_INICIAL, 3)
    cliente1.adicionar_conta(conta1)

    cliente2 = Cliente("987.654.321-00", "Maria Oliveira", "Rua B, 456")
    conta2 = ContaCorrente(cliente2, 2, CHEQUE_ESPECIAL_INICIAL, 3)
    cliente2.adicionar_conta(conta2)

    while True:
        imprimir_menu()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            print(f"Saldo atual: R$ {conta1.consultar_saldo()}")
        elif opcao == 2:
            valor_saque = float(input("Digite o valor do saque: "))
            if conta1.sacar(valor_saque):
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
        elif opcao == 3:
            valor_transferencia = float(input("Digite o valor da transferência: "))
            conta1.transferir(conta2, valor_transferencia)
        elif opcao == 4:
            print("Histórico de transações de João:")
            conta1.historico.exibir_historico()
        elif opcao == 5:
            print("Obrigado por utilizar o Banco do Brasil")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()