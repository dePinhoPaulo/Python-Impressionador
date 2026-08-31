class ContaCorrente:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print("Seu saldo é de: R${:,.2f}".format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def _limite_conta(self):
        self.limite = -100
        return self.limite
    
    def sacar(self, valor):
        if self.saldo - valor < self._limite_conta():
            print("Você não tem saldo sulficiente para sacar esse valor!")
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_cheque_especial(self):
        print("Seu limite de cheque especial é de: R${:,.2f}".format(self._limite_conta()))

#programa
conta_paulo = ContaCorrente('Paulo', '123.456.789.00')

print(conta_paulo.cpf)
print(conta_paulo.saldo)

conta_paulo.depositar(100)
conta_paulo.sacar(54.5)
conta_paulo.sacar(60)

conta_paulo.consultar_saldo()
conta_paulo.consultar_limite_cheque_especial()
