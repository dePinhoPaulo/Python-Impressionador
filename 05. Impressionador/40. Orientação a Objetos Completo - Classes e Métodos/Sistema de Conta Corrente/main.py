from ContasBanco import ContaCorrente, CartaoCredito

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