from datetime import datetime
import pytz

class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime("%d/%m/%y %H:%M:%S")
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print("Seu saldo é de: R${:,.2f}".format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -100
        return self.limite
    
    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não tem saldo sulficiente para sacar esse valor!")
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print("Seu limite de cheque especial é de: R${:,.2f}".format(self._limite_conta()))

    def consultar_transacoes(self):
        print("Histórico de Transações: ")
        print("Valor, Saldo, Data e Hora")
        for transacao in self.transacoes:
            print(transacao)

#programa
conta_paulo = ContaCorrente('Paulo', '123.456.789.00', 1, 21448)

print(conta_paulo.cpf)
print(conta_paulo.saldo)

conta_paulo.depositar(100)
conta_paulo.sacar(54.5)
conta_paulo.sacar(60)

conta_paulo.consultar_saldo()
conta_paulo.consultar_limite_cheque_especial()

print("-" * 25)

print(conta_paulo.consultar_transacoes())