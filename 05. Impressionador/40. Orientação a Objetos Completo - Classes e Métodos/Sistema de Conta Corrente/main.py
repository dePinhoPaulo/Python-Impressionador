from ContasBanco import ContaCorrente, CartaoCredito
from Agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual

# Programa
conta_paulo = ContaCorrente('Paulo', '123.456.789.00', 1, 21448)

# print(conta_paulo._cpf)
# print(conta_paulo._saldo)

# conta_paulo.depositar(100)
# conta_paulo.sacar(54.5)
# conta_paulo.sacar(60)

# conta_paulo.consultar__saldo()
# conta_paulo.consultar__limite_cheque_especial()

# print("-" * 25)

# print(conta_paulo.consultar__transacoes())

# print("-" * 25)

conta_maePaulo = ContaCorrente('Naia', '000.456.000.00', 1, 21450)

# conta_paulo.transferir(50, conta_maePaulo)

# conta_paulo.consultar__transacoes()
# conta_maePaulo.consultar__transacoes()

# help(ContaCorrente)

cartao_paulo = CartaoCredito('Paulo', conta_paulo)

# print(cartao_paulo.conta_corrente.num_conta)
# print(conta_paulo.cartoes[0].numero)
# print(cartao_paulo.cod_seguranca)

# print(cartao_paulo.validade)

cartao_paulo.senha = '4567'

print(cartao_paulo.senha)

print(conta_paulo.__dict__)
print(cartao_paulo.__dict__)


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