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

agencia_1 = Agencia(32671388, 12345678901, 1000)

agencia_1.caixa = 20000
agencia_1.verificar_caixa()

agencia_1.emprestar_dinheiro(10000, 10012345678, 0.02)

print(agencia_1.emprestimos)

agencia_1.adicionar_cliente('Paulo', 10012345678, 1000000)

print(agencia_1.clientes)