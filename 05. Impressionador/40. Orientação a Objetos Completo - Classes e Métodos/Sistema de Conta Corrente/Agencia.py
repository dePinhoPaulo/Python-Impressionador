from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("Caixa abaixo do nivel recomendado. Caixa atual: {}".format(self.caixa))
        else:
            print("O valor do caixa está OK. Caixa atual: {}".format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Emprestimo não e possivel. Dinheiro não disponivel em caixa!")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

# agencia online
class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
 
    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor

# agencia comum
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

# agencia premium
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("Cliente não tem patrimonio minimo para entrar na Agencia Premium!")


if __name__ == '__main__':
    agencia_1 = AgenciaComum(32671388, 12345678901)

    # agencia_1.caixa = 20000
    agencia_1.verificar_caixa()
    print(agencia_1.numero)

    # agencia_1.emprestar_dinheiro(10000, 10012345678, 0.02)

    # print(agencia_1.emprestimos)

    # agencia_1.adicionar_cliente('Paulo', 10012345678, 1000000)

    # print(agencia_1.clientes)

    agencia_virtual_1 = AgenciaVirtual('www.agenciavirtual.com', 22224444, 123456789858)
    agencia_virtual_1.verificar_caixa()
    print(agencia_virtual_1.site)

    agencia_premium_1 = AgenciaPremium(3267999, 12345999991)

    # agencia_1.caixa = 20000
    agencia_premium_1.verificar_caixa()
    print(agencia_premium_1.numero)

    agencia_virtual_1.depositar_paypal(20000)
    print(agencia_virtual_1.caixa)
    print(agencia_virtual_1.caixa_paypal)

    agencia_premium_1.adicionar_cliente('Paulo', 12345678910, 50000000)
    agencia_premium_1.adicionar_cliente('irmao_Paulo', 12345678910, 50000)
    print(agencia_premium_1.clientes)