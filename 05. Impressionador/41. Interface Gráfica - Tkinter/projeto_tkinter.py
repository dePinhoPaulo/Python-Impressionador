import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/json/all') # Requisição de todas medas da API
dicionario_moedas = requisicao.json() # Transformando requisição em um dicionario

lista_moedas = list(dicionario_moedas.keys())

janela = tk.Tk()


janela.title("Ferramenta de cotações de moedas")

# Cotação de 1 Moeda

def pegar_cotacao():
    moeda = combobox_selecionar_moeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:] 
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}' # Retorna uma lista de objetos
    requisica_moeda = requests.get(link)
    cotacao = requisica_moeda.json()
    valor_moeda = cotacao[0]['bid'] # Pegando key referente ao valor de fechamento do dia
    print(valor_moeda)
    label_texto_cotacao['text'] = f"A cotação do {moeda} no dia {data_cotacao} foi de: R${valor_moeda}"

def selecionar_arquivo():
    pass

def atualizar_cotacoes():
    pass

label_cotacao_moeda = tk.Label(text="Cotações de 1 Moeda Específica", borderwidth=2, relief='solid')
label_cotacao_moeda.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_selecionar_moeda = tk.Label(text="Selecione a Moeda: ", anchor='e')
label_selecionar_moeda.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
combobox_selecionar_moeda = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moeda.grid(row=1, column=2, padx=10, pady=10, sticky='nswe')

label_selecionar_dia = tk.Label(text="Selecione o dia que voce quer pegar a cotação: ", anchor='e')
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

label_selecionar_arquivo = tk.Label(text="Selecione um arquivo em excel com as moedas na coluna A: ")
label_selecionar_arquivo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
botao_selecionar_arquivo = tk.Button(text="Clique para selecionar", command=selecionar_arquivo)
botao_selecionar_arquivo.grid(row=5, column=2, padx=10, pady=10, sticky='nswe')

label_arquivo_selecionado = tk.Label(text="Nenhum arquivo selecionado.", anchor='e') # anchor = text align (n, s, w, e)
label_arquivo_selecionado.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

label_data_inicial = tk.Label(text="Data Inicial", anchor='e')
label_data_inicial.grid(row=7, column=0, padx=10, pady=10, sticky='nswe')
calendario_data_inicial = DateEntry(year=2026, locale='pt_br')
calendario_data_inicial.grid(row=7, column=1, padx=10, pady=10, sticky='nswe')

label_data_final = tk.Label(text="Data Final", anchor='e')
label_data_final.grid(row=8, column=0, padx=10, pady=10, sticky='nswe')
calendario_data_final = DateEntry(year=2026, locale='pt_br')
calendario_data_final.grid(row=8, column=1, padx=10, pady=10, sticky='nswe')

label_atualizar_cotacoes = tk.Label(text="")
label_atualizar_cotacoes.grid(row=9, column=1, padx=10, pady=10, sticky='nswe', columnspan=2)
botao_atualizar_cotacoes = tk.Button(text="Atualizar Cotações", command=atualizar_cotacoes)
botao_atualizar_cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky='nswe')

botao_fechar = tk.Button(text="Fechar", command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky='nswe')


janela.mainloop()