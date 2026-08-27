# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes

class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligada = 'desligada'
        self.tamanho = 55
        self.volume = 12
        self.canal = 'Netflix'

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f'Canal alterado para {novo_canal}')

tv_sala = TV()
tv_quarto = TV()

tv_sala.cor = 'branca'
tv_quarto.tamanho = 40

print(tv_quarto.cor)
print(tv_sala.cor)

print(tv_quarto.tamanho)
print(tv_sala.tamanho)

tv_quarto.mudar_canal('HBO Max')

print(tv_quarto.canal)
print(tv_sala.canal)
