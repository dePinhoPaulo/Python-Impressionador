import tkinter as tk

janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure([0], weight=1) # ativa o redmiensionamento autmatico da 1° linha
janela.columnconfigure([0, 1], weight=1) # ativa o redmiensionamento autmatico da 1° e 2° coluna

menssagem = tk.Label(text="Sistema de busca de cotações de moedas!", fg='white', bg='black', width=35, height=5) #fg: letra, bg: fundo, width: largura, height: altura
menssagem.grid(row=0, column=0, columnspan=2, sticky='ewns')

menssagem2 = tk.Label(text="Selecione a moeda desajada:")
menssagem2.grid(row=1, column=0)

moeda = tk.Entry()
moeda.grid(row=1, column=1)


cotacoes = {
    'Dolar': 5.87,
    'Euro': 6.30,
    'Libra': 7.10
}

def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = cotacoes.get(moeda_preenchida)
    label_cotacao = tk.Label(text="Não encontrada!")
    label_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        label_cotacao['text'] = f'Cotação de {moeda_preenchida} é de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()