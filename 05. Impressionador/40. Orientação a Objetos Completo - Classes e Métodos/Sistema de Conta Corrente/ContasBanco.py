from datetime import datetime
import pytz

class ContaCorrente:
    """
    Cria um objeto conta corrente para gerenciar as contas dos clientes.

    Atributos:
        _nome (str): Nome do cliente 
        _cpf (str): CPF do cliente. Deve ser inserido com pontos e traço
        _saldo (float): Saldo atual do cliente
        _limite (float): _saldo negativo maximo parmitido para o cliente
        agencia (int): numero de cadastro da agencia
        num_conta (int): numero de cadastro da conta
        _transacoes (tuple): historioco de transações da conta
    """
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime("%d/%m/%y %H:%M:%S")
    
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []

    def consultar__saldo(self):
        """
        Exibe o _saldo atual da conta corrente.
        """
        print("Seu _saldo é de: R${:,.2f}".format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def limite_conta(self):
        self._limite = -100
        return self._limite
    
    def sacar(self, valor):
        if self._saldo - valor < self.__limite_conta():
            print("Você não tem _saldo sulficiente para sacar esse valor!")
            self.consultar__saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print("Seu _limite de cheque especial é de: R${:,.2f}".format(self.__limite_conta()))

    def consultar__transacoes(self):
        print("Histórico de Transações: ")
        print("Valor, Saldo, Data e Hora")
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

#programa
conta_paulo = ContaCorrente('Paulo', '123.456.789.00', 1, 21448)

print(conta_paulo._cpf)
print(conta_paulo._saldo)

conta_paulo.depositar(100)
conta_paulo.sacar(54.5)
conta_paulo.sacar(60)

conta_paulo.consultar__saldo()
conta_paulo.consultar__limite_cheque_especial()

print("-" * 25)

print(conta_paulo.consultar__transacoes())

print("-" * 25)

conta_maePaulo = ContaCorrente('Naia', '000.456.000.00', 1, 21450)

conta_paulo.transferir(50, conta_maePaulo)

conta_paulo.consultar__transacoes()
conta_maePaulo.consultar__transacoes()

help(ContaCorrente)