import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

lista_moedas = ['USD', 'EUR']

janela = tk.Tk()


janela.title("Ferramenta de cotações de moedas")

# Cotação de 1 Moeda

def pegar_cotacao():
    pass

label_cotacao_moeda = tk.Label(text="Cotações de 1 Moeda Específica", borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionar_moeda = tk.Label(text="Selecione a Moeda: ")
label_selecionar_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
combobox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionar_dia = tk.Label(text="Selecione o dia que voce quer pegar a cotação: ")
label_selecionar_dia.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
calendario_moeda = DateEntry(year=2026, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky='nswe')

label_texto_cotacao = tk.Label(text="")
label_texto_cotacao.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

botao_pegar_cotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegar_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky='nswe')

# Cotação de varias Moedas

label_cotacao_moeda = tk.Label(text="Cotações de Mútiplas Moedas", borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)


janela.mainloop()